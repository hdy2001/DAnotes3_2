import numpy as np
from scipy.io import loadmat
import matplotlib as mpl
import matplotlib.pyplot as plt


def load():
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    mat = loadmat('./data.mat')
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


def ARIMA():
    return


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
    x, y = load()
    draw(x, y)

    # 使用移动平均法后绘图
    new_y = MA(y, 5)
    draw(x, new_y)

    new_y = MA(y, 30)
    draw(x, new_y)

    # 使用指数平均法后绘图
    new_y = EMA(y, 0.2)
    draw(x, new_y)
