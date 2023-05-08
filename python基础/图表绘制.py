'''
常见图表：
条形图
柱状图
折线图
饼图
散点图
面积图
曲面图
圆环图
雷达图
气泡图
股价图
'''

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


class ChartGeneration:
    def __init__(self, title=None):
        # 指定默认字体 下面三条代码用来解决绘图中出现的乱码
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['font.family'] = 'sans-serif'

        # 解决负号'-'显示为方块的问题
        matplotlib.rcParams['axes.unicode_minus'] = False
        self.fig = plt.figure(title)
        self.fig_idx = 0
        self.ax = []

    def chart_setting(self, nrow, ncol, index, configs):
        '''
        图表展示设置
        '''
        self.ax.append(self.fig.add_subplot(nrow, ncol, index, projection=configs['projection']))
        self.ax[self.fig_idx].set_title(configs['title'])  # 设置标题
        self.ax[self.fig_idx].set_xlabel(configs['xlabel'])  # 设置x轴描述
        self.ax[self.fig_idx].set_ylabel(configs['ylabel'])  # 设置y轴描述
        self.ax[self.fig_idx].set_xticklabels(configs['xticklabels'])  # 设置x轴刻度标签
        self.ax[self.fig_idx].set_yticklabels(configs['yticklabels'])  # 设置x轴刻度标签

    def chart_setting1(self, shape, configs):
        '''
        图表展示设置
        '''
        for i in range(len(configs)):
            self.ax.append(plt.subplot2grid(shape, configs[i]['location'], rowspan=configs[i]['rowspan'],
                                            colspan=configs[i]['colspan']))
            self.ax[i].set_title(configs[i]['title'])  # 设置标题
            self.ax[i].set_xlabel(configs[i]['xlabel'])  # 设置x轴描述
            self.ax[i].set_ylabel(configs[i]['ylabel'])  # 设置y轴描述
            self.ax[i].set_xticklabels(configs[i]['xticklabels'])  # 设置x轴刻度标签
            self.ax[i].set_yticklabels(configs[i]['yticklabels'])  # 设置x轴刻度标签

    def show(self):
        '''
        图表绘制展示
        :return:
        '''
        plt.tight_layout()
        plt.show()

    def save(self, outpath):
        plt.savefig(outpath)

    def histogram(self, x, y, **kwargs):
        '''
        直方图
        :return:
        '''
        self.ax[self.fig_idx].hist(x, y, **kwargs)
        self.fig_idx += 1

    def bar_chart(self, x, y, **kwargs):
        '''
        柱状图
        :return:
        '''
        self.ax[self.fig_idx].bar(x, y, **kwargs)
        self.fig_idx += 1

    def line_chart(self, x, y, **kwargs):
        '''
        折线图
        :return:
        '''
        self.ax[self.fig_idx].plot(x, y, **kwargs)
        self.fig_idx += 1

    def pie(self, x, y, **kwargs):
        '''
        饼图
        :return:
        '''
        self.ax[self.fig_idx].pie(y, labels=x, **kwargs)
        self.fig_idx += 1

    def scatter(self, x, y, **kwargs):
        '''
        散点图
        :return:
        '''
        self.ax[self.fig_idx].scatter(x, y, **kwargs)
        self.fig_idx += 1

    def boxplot(self, data_to_plot, **kwargs):
        '''
        箱型图
        :return:
        '''
        self.ax[self.fig_idx].boxplot(data_to_plot, **kwargs)
        self.fig_idx += 1

    def violinplot(self, data_to_plot, **kwargs):
        '''
        提琴图
        :return:
        '''
        self.ax[self.fig_idx].violinplot(data_to_plot, **kwargs)
        self.fig_idx += 1

    def plot3D(self, x, y, z, **kwargs):
        '''
        三维线图
        :return:
        '''

        self.ax[self.fig_idx].plot3D(x, y, z, **kwargs)
        self.fig_idx += 1

    def scatter3D(self, x, y, z, c, **kwargs):
        '''
        3D散点图
        :return:
        '''

        self.ax[self.fig_idx].scatter3D(x, y, z, c=c)
        self.fig_idx += 1

    def contour3D(self, x, y, z, **kwargs):
        '''
        3D等高线图
        :return:
        '''

        self.ax[self.fig_idx].contour3D(x, y, z, **kwargs)
        self.fig_idx += 1

    def plot_wireframe(self, x, y, z, **kwargs):
        '''
        3D线框图
        :return:
        '''

        self.ax[self.fig_idx].plot_wireframe(x, y, z, **kwargs)
        self.fig_idx += 1

    def plot_surface(self, x, y, z, **kwargs):
        '''
        3D曲面图
        :return:
        '''

        self.ax[self.fig_idx].plot_surface(x, y, z, **kwargs)
        self.fig_idx += 1


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))


if __name__ == '__main__':
    cg = ChartGeneration('测试绘图')
    configs = {'title': '折线图', 'xlabel': 'x1', 'ylabel': 'y1',
               'xticklabels': [], 'yticklabels': [], 'projection': None}
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    cg.chart_setting(4, 1, 1, configs)
    cg.line_chart(x, y, color='r', lw=1)

    configs = {'title': '柱状图', 'xlabel': 'x2', 'ylabel': 'y2',
               'xticklabels': [], 'yticklabels': [], 'projection': None}
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    cg.chart_setting(4, 3, 4, configs)
    cg.bar_chart(x, y, color='b', width=0.75)

    configs = {'title': '直方图', 'xlabel': 'x3', 'ylabel': 'y3',
               'xticklabels': [], 'yticklabels': [], 'projection': None}
    x = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
    y = [0, 25, 50, 75, 100]
    cg.chart_setting(4, 3, 5, configs)
    cg.histogram(x, y, histtype='stepfilled', facecolor='r', alpha=0.65)

    configs = {'title': '饼图', 'xlabel': '', 'ylabel': '',
               'xticklabels': [], 'yticklabels': [], 'projection': None}
    x = ['C', 'C++', 'Java', 'Python', 'PHP']
    y = [23, 17, 35, 29, 12]
    cg.chart_setting(4, 3, 6, configs)
    cg.pie(x, y, autopct='%1.2f%%')

    configs = {'title': '散点图', 'xlabel': '', 'ylabel': '',
               'xticklabels': [], 'yticklabels': [], 'projection': None}
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    cg.chart_setting(4, 3, 7, configs)
    cg.scatter(x, y, color='b')

    np.random.seed(10)
    collectn_1 = np.random.normal(100, 10, 200)
    collectn_2 = np.random.normal(80, 30, 200)
    collectn_3 = np.random.normal(90, 20, 200)
    collectn_4 = np.random.normal(70, 25, 200)
    data_to_plot = [collectn_1, collectn_2, collectn_3, collectn_4]
    cg.chart_setting(4, 3, 8, configs)
    cg.boxplot(data_to_plot)

    configs = {'title': '提琴图', 'xlabel': '', 'ylabel': '',
               'xticklabels': [], 'yticklabels': [], 'projection': None}
    cg.chart_setting(4, 3, 9, configs)
    cg.violinplot(data_to_plot)

    configs = {'title': '三维线图', 'xlabel': 'x', 'ylabel': 'y',
               'xticklabels': [], 'yticklabels': [], 'projection': '3d'}
    z = np.linspace(0, 1, 100)
    x = z * np.sin(20 * z)
    y = z * np.cos(20 * z)
    cg.chart_setting(4, 3, 10, configs)
    cg.plot3D(x, y, z)

    configs = {'title': '3D散点图', 'xlabel': 'x', 'ylabel': 'y',
               'xticklabels': [], 'yticklabels': [], 'projection': '3d'}
    z = np.linspace(0, 1, 100)
    x = z * np.sin(20 * z)
    y = z * np.cos(20 * z)
    c = x + y
    cg.chart_setting(4, 3, 11, configs)
    cg.scatter3D(x, y, z, c)

    # # 构建x、y数据
    # configs = {'title': '3D等高线图', 'xlabel': 'x', 'ylabel': 'y',
    #            'xticklabels': [], 'yticklabels': [], 'projection': '3d'}
    # x = np.linspace(-6, 6, 30)
    # y = np.linspace(-6, 6, 30)
    # # 将数据网格化处理
    # X, Y = np.meshgrid(x, y)
    # Z = f(X, Y)
    # cg.chart_setting(4, 3, 12, configs)
    # cg.contour3D(X,Y,Z)

    # 构建x、y数据
    # configs = {'title': '3D线框图', 'xlabel': 'x', 'ylabel': 'y',
    #            'xticklabels': [], 'yticklabels': [], 'projection': '3d'}
    # x = np.linspace(-6, 6, 30)
    # y = np.linspace(-6, 6, 30)
    # # 将数据网格化处理
    # X, Y = np.meshgrid(x, y)
    # Z = f(X, Y)
    # cg.chart_setting(4, 3, 12, configs)
    # cg.plot_wireframe(X,Y,Z)

    # 构建x、y数据
    configs = {'title': '3D曲面图', 'xlabel': 'x', 'ylabel': 'y',
               'xticklabels': [], 'yticklabels': [], 'projection': '3d'}
    # 求向量积(outer()方法又称外积)
    x = np.outer(np.linspace(-2, 2, 30), np.ones(30))
    # 矩阵转置
    y = x.copy().T
    # 数据z
    z = np.cos(x ** 2 + y ** 2)
    cg.chart_setting(4, 3, 12, configs)
    cg.plot_surface(x, y, z)

    cg.save('./../data/plt.png')
    cg.show()
