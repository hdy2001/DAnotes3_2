import pandas as pd
import numpy as np
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression

datas = pd.read_csv('/Users/don/Desktop/DAnotes3_2/模式识别/作业/第三周编程作业/new.txt',
                    sep=' ')
Y = datas.iloc[:, 5]
X = datas.iloc[:, 0:4]
model = LogisticRegression()
model.fit(X, Y)

scores = cross_val_score(model, X, Y, cv=10)
print("准确率:{}".format(scores))
print("平均准确率:{:2f}".format(scores.mean()))