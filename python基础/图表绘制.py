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
    def __init__(self, title=None, **kwargs):
        # 指定默认字体 下面三条代码用来解决绘图中出现的乱码
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['font.family'] = 'sans-serif'

        # 解决负号'-'显示为方块的问题
        matplotlib.rcParams['axes.unicode_minus'] = False
        self.fig = plt.figure(title)
        self.fig.__dict__.update(kwargs)
        self.ax = None

    def chart_setting(self, nrow, ncol, idx, cfg):
        '''
        图表展示设置
        '''
        self.ax = self.fig.add_subplot(nrow, ncol, idx, projection=cfg['projection'])
        self.ax.set_title(cfg['title'])  # 设置标题
        self.ax.set_xlabel(cfg['xlabel'])  # 设置x轴描述
        self.ax.set_ylabel(cfg['ylabel'])  # 设置y轴描述
        self.ax.set_xticklabels(cfg['xticklabels'])  # 设置x轴刻度标签
        self.ax.set_yticklabels(cfg['yticklabels'])  # 设置x轴刻度标签

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
        self.ax.hist(x, y, **kwargs)

    def bar_chart(self, x, y, **kwargs):
        '''
        柱状图
        :return:
        '''
        self.ax.bar(x, y, **kwargs)

    def line_chart(self, x, y, **kwargs):
        '''
        折线图
        :return:
        '''
        self.ax.plot(x, y, **kwargs)

    def pie(self, x, y, **kwargs):
        '''
        饼图
        :return:
        '''
        self.ax.pie(y, labels=x, **kwargs)

    def scatter(self, x, y, **kwargs):
        '''
        散点图
        :return:
        '''
        self.ax.scatter(x, y, **kwargs)

    def boxplot(self, data_to_plot, **kwargs):
        '''
        箱型图
        :return:
        '''
        self.ax.boxplot(data_to_plot, **kwargs)

    def violinplot(self, data_to_plot, **kwargs):
        '''
        提琴图
        :return:
        '''
        self.ax.violinplot(data_to_plot, **kwargs)

    def plot3D(self, x, y, z, **kwargs):
        '''
        三维线图
        :return:
        '''

        self.ax.plot3D(x, y, z, **kwargs)

    def scatter3D(self, x, y, z, c, **kwargs):
        '''
        3D散点图
        :return:
        '''

        self.ax.scatter3D(x, y, z, c=c)

    def contour3D(self, x, y, z, **kwargs):
        '''
        3D等高线图
        :return:
        '''

        self.ax.contour3D(x, y, z, **kwargs)

    def plot_wireframe(self, x, y, z, **kwargs):
        '''
        3D线框图
        :return:
        '''

        self.ax.plot_wireframe(x, y, z, **kwargs)

    def plot_surface(self, x, y, z, **kwargs):
        '''
        3D曲面图
        :return:
        '''

        self.ax.plot_surface(x, y, z, **kwargs)


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))


if __name__ == '__main__':
    cg = ChartGeneration('测试绘图', facecolor='r', dgecolor='g', frameon=True)
    cfg = {'title': '折线图', 'xlabel': 'x1', 'ylabel': 'y1',
               'xticklabels': [], 'yticklabels': [], 'projection': None}
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    cg.chart_setting(4, 1, 1, cfg)
    cg.line_chart(x, y, color='r', lw=1)

    cfg = {'title': '柱状图', 'xlabel': 'x2', 'ylabel': 'y2',
               'xticklabels': [], 'yticklabels': [], 'projection': None}
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    cg.chart_setting(4, 3, 4, cfg)
    cg.bar_chart(x, y, color='b', width=0.75)

    cfg = {'title': '直方图', 'xlabel': 'x3', 'ylabel': 'y3',
               'xticklabels': [], 'yticklabels': [], 'projection': None}
    x = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
    y = [0, 25, 50, 75, 100]
    cg.chart_setting(4, 3, 5, cfg)
    cg.histogram(x, y, histtype='stepfilled', facecolor='r', alpha=0.65)

    cfg = {'title': '饼图', 'xlabel': '', 'ylabel': '',
               'xticklabels': [], 'yticklabels': [], 'projection': None}
    x = ['C', 'C++', 'Java', 'Python', 'PHP']
    y = [23, 17, 35, 29, 12]
    cg.chart_setting(4, 3, 6, cfg)
    cg.pie(x, y, autopct='%1.2f%%')

    cfg = {'title': '散点图', 'xlabel': '', 'ylabel': '',
               'xticklabels': [], 'yticklabels': [], 'projection': None}
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    cg.chart_setting(4, 3, 7, cfg)
    cg.scatter(x, y, color='b')

    np.random.seed(10)
    collectn_1 = np.random.normal(100, 10, 200)
    collectn_2 = np.random.normal(80, 30, 200)
    collectn_3 = np.random.normal(90, 20, 200)
    collectn_4 = np.random.normal(70, 25, 200)
    data_to_plot = [collectn_1, collectn_2, collectn_3, collectn_4]
    cg.chart_setting(4, 3, 8, cfg)
    cg.boxplot(data_to_plot)

    cfg = {'title': '提琴图', 'xlabel': '', 'ylabel': '',
               'xticklabels': [], 'yticklabels': [], 'projection': None}
    cg.chart_setting(4, 3, 9, cfg)
    cg.violinplot(data_to_plot)

    cfg = {'title': '三维线图', 'xlabel': 'x', 'ylabel': 'y',
               'xticklabels': [], 'yticklabels': [], 'projection': '3d'}
    z = np.linspace(0, 1, 100)
    x = z * np.sin(20 * z)
    y = z * np.cos(20 * z)
    cg.chart_setting(4, 3, 10, cfg)
    cg.plot3D(x, y, z)

    cfg = {'title': '3D散点图', 'xlabel': 'x', 'ylabel': 'y',
               'xticklabels': [], 'yticklabels': [], 'projection': '3d'}
    z = np.linspace(0, 1, 100)
    x = z * np.sin(20 * z)
    y = z * np.cos(20 * z)
    c = x + y
    cg.chart_setting(4, 3, 11, cfg)
    cg.scatter3D(x, y, z, c)

    # # 构建x、y数据
    # cfg = {'title': '3D等高线图', 'xlabel': 'x', 'ylabel': 'y',
    #            'xticklabels': [], 'yticklabels': [], 'projection': '3d'}
    # x = np.linspace(-6, 6, 30)
    # y = np.linspace(-6, 6, 30)
    # # 将数据网格化处理
    # X, Y = np.meshgrid(x, y)
    # Z = f(X, Y)
    # cg.chart_setting(4, 3, 12, cfg)
    # cg.contour3D(X,Y,Z)

    # 构建x、y数据
    # cfg = {'title': '3D线框图', 'xlabel': 'x', 'ylabel': 'y',
    #            'xticklabels': [], 'yticklabels': [], 'projection': '3d'}
    # x = np.linspace(-6, 6, 30)
    # y = np.linspace(-6, 6, 30)
    # # 将数据网格化处理
    # X, Y = np.meshgrid(x, y)
    # Z = f(X, Y)
    # cg.chart_setting(4, 3, 12, cfg)
    # cg.plot_wireframe(X,Y,Z)

    # 构建x、y数据
    cfg = {'title': '3D曲面图', 'xlabel': 'x', 'ylabel': 'y',
               'xticklabels': [], 'yticklabels': [], 'projection': '3d'}
    # 求向量积(outer()方法又称外积)
    x = np.outer(np.linspace(-2, 2, 30), np.ones(30))
    # 矩阵转置
    y = x.copy().T
    # 数据z
    z = np.cos(x ** 2 + y ** 2)
    cg.chart_setting(4, 3, 12, cfg)
    cg.plot_surface(x, y, z)

    cg.save('./../data/plt.png')
    cg.show()
