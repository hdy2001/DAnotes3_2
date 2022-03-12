import pandas as pd
import numpy as np
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression

# 读取并对数据进行分类
datas = pd.read_csv('/Users/don/Desktop/DAnotes3_2/模式识别/作业/第三周编程作业/new.txt',
                    sep=' ')
Y = datas.iloc[:, 5]
X = datas.iloc[:, 0:5]


def mean(myX):
    return np.mean(myX, 0)


def S(myX):
    return np.stack([
        np.matmul((item - mean(myX)).reshape(5, 1),
                  (item - mean(myX)).reshape(1, 5)) for item in myX
    ]).sum(axis=0)
    # return np.dot((myX - mean(myX)).T, (myX - mean(myX)))


# 算系数有一点问题
def omega_n(X_1, X_2):
    _mean = (mean(X_1) - mean(X_2)).values
    _mean = _mean.reshape(_mean.shape[0], 1)
    A = np.linalg.inv(S(np.array(X_1)) + S(np.array(X_2)))
    print(np.dot(A, np.linalg.inv(A)))
    return np.dot(A, _mean)


def omega_0(Y_1, Y_2):
    N = len(datas)
    N1 = len(Y_1)
    N2 = len(Y_2)
    return -(N1 * np.mean(Y_1) + N2 * np.mean(Y_2)) / N


kf = KFold(n_splits=10, shuffle=False)
acc = []

for train_index, test_index in kf.split(datas):
    datas_train = datas.iloc[train_index]
    data_1 = datas_train[datas_train.iloc[:, 5] == 1]
    data_2 = datas_train[datas_train.iloc[:, 5] == 0]
    x_test = X.iloc[test_index]
    y_test = Y.iloc[test_index]
    Y_1 = data_1.iloc[:, 5]
    X_1 = data_1.iloc[:, 0:5]
    Y_2 = data_2.iloc[:, 5]
    X_2 = data_2.iloc[:, 0:5]
    omega = omega_n(X_1, X_2)
    omega_ = omega_0(Y_1, Y_2)
    predicts = np.dot(x_test, omega) + omega_
    predicts = (predicts > 0).reshape(-1)
    acc.append(float(np.sum(predicts == y_test)) / float(len(predicts)))
print(acc)
