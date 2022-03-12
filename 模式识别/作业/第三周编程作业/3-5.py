import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

datas = pd.read_csv('模式识别/作业/第三周编程作业/prostate_train.txt', sep='\t')
datas_test = pd.read_csv('模式识别/作业/第三周编程作业/prostate_test.txt', sep='\t')
y = datas.iloc[:, 4]
x = datas.iloc[:, 0:3]

y_test = datas_test.iloc[:, 4]
x_test = datas_test.iloc[:, 0:3]

y = y[:, np.newaxis]
y_test = y_test[:, np.newaxis]

model = LinearRegression()
model.fit(x, y)
predicts = model.predict(x)
R2 = model.score(x, y)  # 拟合程度 R2
print('R2 = %.3f' % R2)  # 输出 R2
RSS = np.sum((predicts - y) * (predicts - y))
print('RSS = %.3f' % RSS)

predicts_test = model.predict(x_test)
R2_test = model.score(x_test, y_test)  # 拟合程度 R2
print('R2 = %.3f' % R2_test)  # 输出 R2
RSS_test = np.sum((predicts_test - y_test) * (predicts_test - y_test))
print('RSS = %.3f' % RSS_test)
