import csv


class CSVOperation():
    def __init__(self, filename):
        self.filename = filename

    def read_csv(self):
        '''获取csv中所有数据'''
        with open(self.filename, 'r', encoding='utf-8') as f:
            cb = csv.reader(f)  # 实例化reader对象
            header = next(cb)  # 获取表头，并将指针转向下一行
            list_dict = []
            for row in cb:
                list_dict.append(dict(zip(header, row)))
            print(list_dict)
            return list_dict

    def read_row(self, index):
        return self.read_csv()[index - 1]

    def write_csv(self, headers, values, data_type, mode='w'):
        with open(self.filename, mode=mode, encoding='utf-8', newline='') as f:
            # newline=‘’参数可以使每次写入数据不会产生空行
            if data_type == 'tuple':
                writer = csv.writer(f)
                writer.writerow(headers)
                writer.writerows(values)
            elif data_type == 'dict':
                writer = csv.DictWriter(f, headers)
                writer.writeheader()  # 写入表头
                writer.writerows(values)  # 写入数据
            else:
                print("数据类型错误，请确认！")


if __name__ == '__main__':
    csv_ob = CSVOperation('../../data/test.csv')
    values = [
        {'id': 1, 'name': 'dog', "age": 18},
        {'id': 2, 'name': 'cat', "age": 19},
        {'id': 3, 'name': 'dog', "age": 20},
    ]
    csv_ob.write_csv(headers=['id', 'name', 'age'], values=values, data_type='dict')
    csv_ob.read_csv()
