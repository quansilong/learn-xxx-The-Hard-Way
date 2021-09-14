#!/usr/bin/python3
# -*- coding: utf-8 -*- 
#
"""

Usage:
  list_gaussian_input.py <options> dictionary

Options:
  -a  --input                    all gaussian input files
  -b  --not_normal_end_input     all gaussian input files without normal termination
  -h  --help                     list this help
  --check                        check whether all gaussian input files are normal-termination



Auther: LiuGaoyong
E-mial:
  liugaoyong_88@163.com
  liugaoyong88@gmail.com
2019-05-01 at Nanjing,China
Based on Python3

"""

import os

def all_files(dir):	# 获取所有文件绝对列表
    all_files_list=[]
    for root,dirs,files in os.walk( dir ):                       
        for fileObj in files:
            all_files_list.append(os.path.join(root,fileObj))
    return all_files_list

def all_gjf(all_files_list):	# 获取所有gjf文件列表
    all_gjf_list=[]
    for i in all_files_list:
        if 'gjf' in i:
            all_gjf_list.append(i)
        elif 'com' in i:
            all_gjf_list.append(i)
        else:
            pass
    return all_gjf_list

def last_line_of_file(file_name): 		# 读取文件最后一行
    with open(file_name, 'rb') as f:
        off = -50
        while True:
            f.seek(off, 2)              #seek(off, 2)表示文件指针：从文件末尾(2)开始向前50个字符(-50)
            lines = f.readlines()       #读取文件指针范围内所有行
            if len(lines)>=2:           #判断是否最后至少有两行，这样保证了最后一行是完整的
                last_line = lines[-1]   #取最后一行
                break
            off *= 2
    return str(last_line)

def all_not_normal_end_gjf(all_gjf_list):	# 获取所有非正常结束的gjf
    all_not_normal_end_gjf=[]
    for i in all_gjf_list:
        if os.path.exists(i[:-3]+'log'):
            last_line = last_line_of_file(i[:-3]+'log')
            if 'Normal' not in last_line:
                all_not_normal_end_gjf.append(i)
        else:
            all_not_normal_end_gjf.append(i)
    return all_not_normal_end_gjf

#---------------------------------------

if __name__ == "__main__":
    import sys
    dir = os.path.abspath(sys.argv[2])
    all_files_list = all_files(dir)
    #-----------------------------------
    if sys.argv[1] in ('-a','--input','--all_input'):
        for i in all_gjf(all_files_list):
            print(i)
    elif sys.argv[1] in ('-b', '--not_normal_end_input'):
        for i in all_not_normal_end_gjf(all_gjf(all_files_list)):
            print(i)
    elif sys.argv[1] in ('--check'):
        for i in all_gjf(all_files_list):
            print('\n',i)
            if os.path.exists(i[:-3]+'log'):
                print(' '+ i[:-3]+'log')
                print('    ', last_line_of_file(i[:-3]+'log'))
            else:
                print('    There is not its log file.')
        print()
    elif sys.argv[1] in ('-h', '--help'):
        print(__doc__)
    else:
        print('Error: There are not this option.', __doc__ )
