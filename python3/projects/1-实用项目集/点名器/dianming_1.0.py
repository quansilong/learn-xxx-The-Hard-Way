import tkinter as tk
import random
import xlrd

workbook = xlrd.open_workbook("name.xls")  # 读取表格
Data_sheet = workbook.sheets()[0]          # 读取sheet1
num_list = []                              # 读取第一列（学号）
for i in range(len(Data_sheet.col_values(0))):         # 化浮点数为字符串
    num_list.append( str(int(Data_sheet.col_values(0)[i])) + '  ' + Data_sheet.col_values(1)[i] )
    
#print(num_list)


name_list = num_list      
data = set()  # 一个空set保存选过的同学
# print(num_list, name_list, data, type(num_list[0]), type(name_list[0]) )

root = tk.Tk()
root.title("点名册")
root.geometry('500x150') 
global var
var = tk.StringVar()
on_strat = False
l = tk.Label(root, textvariable=var, font=('Arial', 35), width=15, height=2)
l.pack()

def start():
    try:
        rdata = random.choice(name_list)
        if on_strat==False:
            name_list.remove(rdata)
            #print(rdata)
            if rdata not in data:
                    var.set(rdata)
                    data.add(rdata)
        if len(name_list)==0:
            var.set("所有同学已经点完")
    except ValueError as e:
        var.set("所有同学已经点完")
B = tk.Button(root, text="Start", command=start)
B.pack()

# 添加背景音乐
# pygame.init()
# music = pygame.mixer.music.load('bg.mp3')
# pygame.mixer.music.play(-1, 100)
# screen = pygame.display.set_mode((800, 600))
 
root.mainloop()