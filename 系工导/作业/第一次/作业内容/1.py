import numpy as np
from scipy.io import loadmat
import matplotlib as mpl
import matplotlib.pyplot as plt
from itertools import chain
import statsmodels.api as sm
import seaborn as sns
import statsmodels.tsa.api as smt
import pandas as pd


# 加载数据的函数
def load():
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    mat = loadmat('/Users/don/Desktop/DAnotes3_2/系工导/作业/第一次/作业内容/data.mat')
    y = mat['data']
    y = np.reshape(y, len(y))
    x = np.arange(len(y))
    return x, y


# 移动平均法
def MA(y, N):
    ans = np.convolve(y, np.ones(N) / N)
    sum = 0
    for i in range(N):
        sum += y[i]
        ans[i] = sum / (i + 1)
    return ans[0:len(y)]


# 指数平均法
def EMA(y, alpha):
    ans = [0] * len(y)
    ans[0] = y[0]
    y_hat = ans[0]
    for i in range(1, len(y)):
        ans[i] = alpha * y[i] + (1 - alpha) * y_hat
        y_hat = ans[i]
    return ans


# ARIMA方法
def ARIMA(y):
    data = pd.DataFrame({"流量": y})
    predicts = sm.tsa.ARIMA(data, order=(8, 0, 7)).fit()
    predict_sunspots = predicts.predict(start=1, end=2600, dynamic=False)
    _, ax = plt.subplots(figsize=(12, 8))
    ax = data.plot(ax=ax)
    predict_sunspots.plot(ax=ax)
    plt.xlabel("采样时间点（间隔30秒）")
    plt.ylabel("高速公路车流量（辆/小时）")
    plt.legend(['平滑前', '平滑后'])
    plt.title("高速公路车流量变化曲线")
    plt.xlim((0, 3000))
    plt.ylim((0, 8000))
    plt.grid()
    plt.show()


def draw(x, y):
    plt.plot(x, y)
    plt.xlabel('采样时间点（间隔30秒）')
    plt.ylabel('高速公路车流量（辆/小时）')
    plt.title('高速公路车流量变化曲线')
    plt.xlim((0, 3000))
    plt.ylim((0, 8000))
    plt.grid()
    plt.show()


if __name__ == '__main__':
    # 加载数据
    x, y = load()
    # draw(x, y)

    # # 使用移动平均法后绘图
    # new_y = MA(y, 5)
    # draw(x, new_y)

    # new_y = MA(y, 30)
    # draw(x, new_y)

    # 使用指数平均法后绘图
    # new_y = EMA(y, 0.2)
    # draw(x, new_y)

    # new_y = EMA(y, 0.05)
    # draw(x, new_y)
    ARIMA(y)