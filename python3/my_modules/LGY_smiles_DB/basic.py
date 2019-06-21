#!/bin/python
# -*- coding: utf-8 -*- 
#
# Auther: LiuGaoyong
# E-mial: liugaoyong_88@163.com
#         liugaoyong88@gmail.com
#
# 2019-03-28 at NJU-HXL-F409
# Based on Python3


import pybel
import openbabel


def smidb_read_2_list(filename_str):
    with open(filename_str) as f:
        data = f.readlines()
    all_mol = []
    for i2 in data:
        index =  i2.split(",")[0]
        reaction_smi = i2.split(",")[1].split("|")[0]
        mol= (index, reaction_smi)
        all_mol.append(mol)
    return all_mol

def rsmi_write_2_rcan_list(rsmi_str):
    reactant, agent, product = rsmi_str.split(">")
    rsmi_str2 = reactant+ "." +agent+ "."+ product
    #print(rsmi_str2)
    rcan_list=[]
    for i in rsmi_str2.split("."):
        mols = pybel.readstring("smi", i)
        rcan_list.append(mols.write("can")[:-2])
    return rcan_list

def search_rsmiDB(smi_mol, DB_list):
    pass


def gaussian_output_2_smi_str(filename_str):
    mols = next(pybel.readfile("gal", filename_str))
    return mols.write("smi")






if __name__=="__main__":
    data = smidb_read_2_list(r"D:\LiuGaoyong\Documents\github\learn-xxx-The-Hard-Way\python3\projects\ChemInformatics\copy_train - 副本.txt")
    #pprint.pprint(data[0][1])
    #pprint.pprint(rsmi_write_2_rcan_list(data[0][1]))
    mol = pybel.readstring("smi", "c1cc(F)ccc1").write("can")[:-2]
    print(mol)
    a= gaussian_output_2_smi_str("20171016_84008-04-8_gas_iso2.log")
	#print(a)
'''
    for i in data:
        rcan_list = rsmi_write_2_rcan_list(i[1])
        if mol in rcan_list :
            print(i)
            print(rcan_list)
    
'''
	
    
    
    
    
    
    
    
    

