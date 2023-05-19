# coding:utf-8
from allpairspy import AllPairs
from python基础.文件操作.openpyxl操作excel import ExcelOperation


def is_valid_combination(row):
    '''
    无效测试案例过滤
    :param row:
    :return:
    '''
    eo = ExcelOperation(file, '无效组合')
    datas = eo.read_area(row_start_index=2)
    n = len(row)
    if n == len(datas[0]):
        for data in datas:
            temp = 0
            for i in range(n):
                if data[i] and row[i] in data[i].split(';'):
                    temp += 1
                elif data[i] is None:
                    temp += 1
                else:
                    continue
            if temp == n:
                return False
            else:
                continue

    return True


file = '.././data/正交案例生成器2.xlsx'
eo = ExcelOperation(file, '因子表')
keys = eo.read_col(1)[1:]
print(keys)
values = eo.read_area(row_start_index=2, col_start_index=2)
parameters = []
for v in values:
    parameters.append(v[0].strip().split(';'))
print(parameters)
print("PAIRWISE:")
cases = []
for i, pairs in enumerate(AllPairs(parameters, filter_func=is_valid_combination)):
    print("用例编号{:2d}: {}".format(i, pairs))
    cases.append(pairs)

cases.sort()
eo.change_workbook(file, '生成的案例')
eo.write_row(keys, 1)
eo.write_area(cases, 2, 1)

# eo.add_sheet('生成的案例')
# eo2 = ExcelOperation(file, '生成的案例')
# eo2.write_row(keys, 1)
# eo2.write_area(cases, 2, 1)
