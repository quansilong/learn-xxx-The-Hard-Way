#!/bin/python
# -*- coding: utf-8 -*- 
#
# Auther: LiuGaoyong
# E-mial: liugaoyong_88@163.com
#         liugaoyong88@gmail.com
#
# 2019-03-28 at NJU-HXL-F409
# Based on Python3


import os


def folder2List(dirPath):
    fileList=[]
    for root,dirs,files in os.walk(dirPath):    #root is always fileObj's father path
        for fileObj in files:                   #root 永远是 fileObj 的父路径
            fileList.append(os.path.join(root,fileObj))
    return (fileList, len(fileList))
	
if __name__ == "__main__":
	import pprint
	pprint.pprint(folder2List(r"D:\Python-Anaconda3\0-LGY"))