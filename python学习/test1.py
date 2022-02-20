import csv
import os
import time

import pandas as pd
class CSVClass:
    def __init__(self,fp):
        self.fp=fp
        self.df=pd.read_csv(self.fp,encoding='gbk')
        self.new_file=self.fp.rsplit('.',maxsplit=1)[0]+time.strftime('%Y%m%d%H%M%S',time.localtime())+'.csv'
        self.csv_file=open(self.new_file, 'a',newline='')
        self.csv_writer= csv.writer(self.csv_file)
        self.csv_writer.writerow(self.df.columns)

    def write_row(self,data):
        self.csv_writer.writerow(data)
        self.csv_file.flush()

    def __del__(self):
        self.csv_file.close()
        self.df.close()


if __name__ == '__main__':
    csv_ins=CSVClass(r'D:\CODE\CodeTest\python学习\test.csv')
    for i in range(csv_ins.df.shape[0]):
        print(f'NO.{i}')
        time.sleep(10)
        csv_ins.write_row(csv_ins.df.iloc[i])
    csv_ins.csv_file.close()
