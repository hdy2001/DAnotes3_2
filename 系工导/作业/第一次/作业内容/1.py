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
def MA():
    return


# 指数平均法
def EMA():
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
