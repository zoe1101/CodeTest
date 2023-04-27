import openpyxl
import xlrd
import xlwt
from xlutils.copy import copy
import os

class ExcelOperation():
    def __init__(self, file_path, sheet_name="Sheet1", read_or_write='read'):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.workbook = None
        if read_or_write == 'read':
            self.workbook = xlrd.open_workbook(self.file_path)
            self.worksheet = self.workbook.sheet_by_name(self.sheet_name)
        elif read_or_write == 'write':
            if os.path.exists(self.file_path):
                self.workbook = xlrd.open_workbook(self.file_path)
            else:
                self.workbook = xlwt.Workbook(encoding='utf-8')
            self.worksheet = {}
            self.workstyle = xlwt.XFStyle()  # 初始化样式

    def get_rows(self):
        '''行数统计'''
        return self.worksheet.nrows

    def get_cols(self):
        '''列数统计 '''
        return self.worksheet.ncols

    def read_row(self, row_index):
        return self.worksheet.row_values(row_index)

    def write_row(self, value, row_index, col_index, sheet_name):
        __row = row_index
        __col = col_index
        for __value in value:
            self.write_cell(__value, __row, __col, sheet_name)
            __col = __col + 1

    def read_col(self, col_index):
        return self.worksheet.col_values(col_index)

    def write_col(self, value, row_index, col_index, sheet_name):
        pass
        __row = row_index
        __col = col_index
        for __value in value:
            self.write_cell(__value, __row, __col, sheet_name)
            __row = __row + 1

    def read_cell(self, row_index, col_index):
        return self.worksheet.cell_value(row_index, col_index)

    def write_cell(self, value, row_index, col_index, sheet_name):
        self.worksheet[sheet_name].write(row_index, col_index, value, self.workstyle)

    def read_area(self, row_start_index, row_end_index, col_start_index, col_end_index):
        """
        获取某一个区域的所有值构成的二维列表
        :param row_start_index: 该区域行号的起始值
        :param row_end_index: 该区域行号的结束值
        :param col_start_index: 该区域列号的起始值
        :param col_end_index: 该区域列号的结束值
        :return: 返回该区域的值构成的列表
        """
        res = []
        for row in range(row_start_index, row_end_index + 1):
            res.append(self.worksheet.row_values(row, start_colx=col_start_index, end_colx=col_end_index))

        return res

    def write_area(self, area_value, row_index, col_index, sheet_name, one_row_font_num=30):
        pass
        __row = row_index
        __col = col_index
        # 遍历传入进来的某一个区域的所有值构成的二维列表，每次遍历得到一行的数据
        for __row_list in area_value:
            # 遍历每一行数据 然后依次一个单元格一个单元格的写入数据 ，每次遍历得到一行中的某一列的数据
            for cell_value in __row_list:
                self.set_col_width(__col, one_row_font_num, sheet_name)
                self.write_cell(cell_value, __row, __col, sheet_name)
                __col = __col + 1
            __col = col_index  # 换行
            __row = __row + 1

    def add_sheet(self, sheet_name):
        wb = xlrd.open_workbook(self.file_path)
        newb = copy(wb)  # 复制原有表
        self.worksheet[sheet_name] = newb.add_sheet(sheet_name)
        self.workbook=newb


    def set_col_width(self, col_index, one_row_font_num, sheet_name):
        self.worksheet[sheet_name].col(col_index).width = 256 * one_row_font_num
        self.workstyle.alignment.wrap = 1

    def set_style(self, name='Arial', height=200, colour_index=0x7FFF, bold=False, underline=False, italic=False,
                  borders=True, borders_colour_index=0x40,
                  backgroud_color=0x01, alignment=None):
        # 初始化样式
        __style = xlwt.XFStyle()

        #  字体设置
        __font = xlwt.Font()  # 为样式创建字体
        # 字体
        __font.name = name
        __font.height = height
        # 颜色索引
        __font.colour_index = colour_index
        # 颜色也可以从定义好的map中去取
        # __font.colour_index = xlwt.Style.colour_map['red']

        # 加粗
        __font.bold = bold
        # 下划线
        __font.underline = underline
        # 斜体
        __font.italic = italic
        __style.font = __font

        # 设置单元格背景颜色
        pattern = xlwt.Pattern()
        # 设置背景颜色的模式
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        # 背景颜色
        pattern.pattern_fore_colour = backgroud_color
        __style.pattern = pattern

        # 设置单元格的对齐方式，默认水平垂直居中
        if alignment is None:
            __alignment = xlwt.Alignment()
            # 水平居中
            __alignment.horz = xlwt.Alignment.HORZ_CENTER
            # 垂直居中
            __alignment.vert = xlwt.Alignment.VERT_CENTER
            __style.alignment = __alignment
        else:
            __style.alignment = alignment

        #  边框设置
        if borders is True:
            __borders = xlwt.Borders()
            __borders.left = xlwt.Borders.MEDIUM
            __borders.right = xlwt.Borders.MEDIUM
            __borders.top = xlwt.Borders.MEDIUM
            __borders.bottom = xlwt.Borders.MEDIUM
            __borders.left_colour = borders_colour_index
            __borders.right_colour = borders_colour_index
            __borders.top_colour = borders_colour_index
            __borders.bottom_colour = borders_colour_index
            __style.borders = __borders

        self.workstyle = __style  # 修改字体格式
        return __style

    def save_excel(self):
        """
        保存表格
        :param path: 保存的路径
        """
        self.workbook.save(self.file_path)


if __name__ == '__main__':
    sheet_r = ExcelOperation("../../data/test.xls", "Sheet1")
    data = sheet_r.read_area(1, 1, 0, 2)
    print(data)
    sheet_w = ExcelOperation(file_path='../../data/test.xls', read_or_write='write')
    sheet_w.add_sheet('test')
    sheet_w.save_excel()
    sheet_w.write_area(data, 2, 2, 'test', 15)
    sheet_w.save_excel()
