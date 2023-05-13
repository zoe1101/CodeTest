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
    def __init__(self):
        # 指定默认字体 下面三条代码用来解决绘图中出现的乱码
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['font.family'] = 'sans-serif'

        # 解决负号'-'显示为方块的问题
        matplotlib.rcParams['axes.unicode_minus'] = False
        self.fig_idx = 0
        self.ax = []

    def chart_setting(self, shape, configs):
        '''
        图表展示设置
        '''
        self.ax.append(plt.subplot2grid(shape, configs['location'], rowspan=configs['rowspan'],
                                        colspan=configs['colspan']))
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
        self.ax[self.fig_idx].boxplot(data_to_plot)
        self.fig_idx += 1

    def violinplot(self, data_to_plot, **kwargs):
        '''
        提琴图
        :return:
        '''
        self.ax[self.fig_idx].violinplot(data_to_plot)
        self.fig_idx += 1


if __name__ == '__main__':
    cg = ChartGeneration()
    shape = (3, 3)
    # configs = [{'location': (0, 0), 'rowspan': 1, 'colspan': 1, 'title': 'fig1', 'xlabel': 'x1', 'ylabel': 'y1',
    #             'xticklabels': [], 'yticklabels': []},
    #            {'location': (0, 1), 'rowspan': 1, 'colspan': 1, 'title': 'fig2', 'xlabel': 'x2', 'ylabel': 'y2',
    #             'xticklabels': [], 'yticklabels': []},
    #            {'location': (1, 0), 'rowspan': 1, 'colspan': 1, 'title': 'fig3', 'xlabel': 'x3', 'ylabel': 'y3',
    #             'xticklabels': [], 'yticklabels': []},
    #            {'location': (1, 1), 'rowspan': 1, 'colspan': 1, 'title': 'fig4', 'xlabel': '', 'ylabel': '',
    #             'xticklabels': [], 'yticklabels': []},
    #            {'location': (2, 0), 'rowspan': 1, 'colspan': 1, 'title': 'fig5', 'xlabel': '', 'ylabel': '',
    #             'xticklabels': [], 'yticklabels': []}, ]

    configs = {'location': (0, 0), 'rowspan': 1, 'colspan': 1, 'title': '折线图', 'xlabel': 'x1', 'ylabel': 'y1',
               'xticklabels': [], 'yticklabels': []}
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    cg.chart_setting(shape, configs)
    cg.line_chart(x, y, color='r', lw=1)

    configs = {'location': (0, 1), 'rowspan': 1, 'colspan': 1, 'title': '柱状图', 'xlabel': 'x2', 'ylabel': 'y2',
               'xticklabels': [], 'yticklabels': []}
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    cg.chart_setting(shape, configs)
    cg.bar_chart(x, y, color='b', width=0.75)

    configs = {'location': (1, 0), 'rowspan': 1, 'colspan': 1, 'title': '直方图', 'xlabel': 'x3', 'ylabel': 'y3',
               'xticklabels': [], 'yticklabels': []}
    x = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
    y = [0, 25, 50, 75, 100]
    cg.chart_setting(shape, configs)
    cg.histogram(x, y, histtype='stepfilled', facecolor='r', alpha=0.65)

    configs = {'location': (1, 1), 'rowspan': 1, 'colspan': 1, 'title': '饼图', 'xlabel': '', 'ylabel': '',
               'xticklabels': [], 'yticklabels': []}
    x = ['C', 'C++', 'Java', 'Python', 'PHP']
    y = [23, 17, 35, 29, 12]
    cg.chart_setting(shape, configs)
    cg.pie(x, y, autopct='%1.2f%%')

    configs = {'location': (2, 0), 'rowspan': 1, 'colspan': 1, 'title': '散点图', 'xlabel': '', 'ylabel': '',
               'xticklabels': [], 'yticklabels': []}
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    cg.chart_setting(shape, configs)
    cg.scatter(x, y, color='b')

    np.random.seed(10)
    collectn_1 = np.random.normal(100, 10, 200)
    collectn_2 = np.random.normal(80, 30, 200)
    collectn_3 = np.random.normal(90, 20, 200)
    collectn_4 = np.random.normal(70, 25, 200)
    data_to_plot = [collectn_1, collectn_2, collectn_3, collectn_4]
    cg.chart_setting(shape, configs)
    cg.boxplot(data_to_plot)

    configs = {'location': (2, 2), 'rowspan': 1, 'colspan': 1, 'title': '提琴图', 'xlabel': '', 'ylabel': '',
               'xticklabels': [], 'yticklabels': []}
    cg.chart_setting(shape, configs)
    cg.violinplot(data_to_plot)

    cg.save('./../data/plt.png')
    cg.show()
