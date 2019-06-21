import tkinter as tk
import random
import xlrd

workbook = xlrd.open_workbook("name.xls")  # 读取表格
Data_sheet = workbook.sheets()[0]          # 读取sheet1
num_list = []                              # 读取第一列（学号）
for i in range(len(Data_sheet.col_values(0))):         # 化浮点数为字符串
    num_list.append( str(int(Data_sheet.col_values(0)[i])) + '  ' + Data_sheet.col_values(1)[i] )

rdata = random.sample(num_list,24)

fileObject = open('sampleList.txt', 'w', encoding ='utf-8')
for name in rdata:
    fileObject.write(name)
    fileObject.write('\n')
fileObject.close()