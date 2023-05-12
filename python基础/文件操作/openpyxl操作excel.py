import openpyxl


class ExcelOperation():
    def __init__(self, file_path, sheet_name="Sheet1"):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.workbook = openpyxl.load_workbook(self.file_path)
        if self.sheet_name is None:
            self.worksheet = self.workbook.active  # active默认读取第一个表单
        else:
            self.worksheet = self.workbook[self.sheet_name]  # 读取指定表单

    def get_rows(self):
        '''行数统计'''
        return self.worksheet.max_row

    def get_cols(self):
        '''列数统计 '''
        return self.worksheet.max_column

    def read_row(self, row_index):
        res = []
        for col in range(self.get_cols()):
            res.append(self.read_cell(row_index, col + 1))
        return res

    def write_row(self, value, row_index):
        for col in range(self.get_cols()):
            self.worksheet.cell(row_index, col + 1).value = value[col]
        self.save_excel()

    def read_col(self, col_index):
        res = []
        for row in range(self.get_rows()):
            res.append(self.read_cell(row + 1, col_index))
        return res

    def write_col(self, value, col_index):
        for row in range(self.get_rows()):
            self.worksheet.cell(row + 1, col_index).value = value[row]
        self.save_excel()

    def read_cell(self, row_index, col_index):
        return self.worksheet.cell(row_index, col_index).value

    def write_cell(self, value, row_index, col_index):
        self.worksheet.cell(row_index, col_index).value = value
        self.save_excel()

    def read_area(self, row_start_index, row_end_index, col_start_index, col_end_index):
        res = []
        for row in range(row_start_index, row_end_index + 1):
            temp = []
            for col in range(col_start_index, col_end_index + 1):
                temp.append(self.read_cell(row, col))
            res.append(temp)
        return res

    def write_area(self, area_value, row_start_index, col_start_index):
        m, n = len(area_value), len(area_value[0])
        for i in range(m):
            for j in range(n):
                self.worksheet.cell(row_start_index + i, col_start_index + j).value = area_value[i][j]
        self.save_excel()

    def save_excel(self):
        """
        保存表格
        :param path: 保存的路径
        """
        self.workbook.save(self.file_path)

    def set_style(self):
        '''
        表格样式设置
        :return:
        '''
        pass

    def add_sheet(self, sheet_name):
        pass

    def delete_sheet(self, sheet_name):
        pass

    def update_sheet_name(self, ori_name, new_name):
        pass


if __name__ == '__main__':
    sheet = ExcelOperation("../../data/test.xlsx", "Sheet1")
    data = sheet.read_area(1, 1, 1, 3)
    print(data)
    sheet.write_area(data, 4, 1)
