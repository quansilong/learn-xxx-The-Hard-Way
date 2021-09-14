#!/usr/bin/env python
import pybel

#读入数据
with open("./copy_train - 副本.txt") as f:
    data = f.readlines()
    
# 数据结构重新架构：
#    (  (index, smiles)
#        ... ...    )
all_mol = []
for i2 in data:
    index =  i2.split(",")[0]
    reaction_smi = i2.split(",")[1].split("|")[0]
    mol= (index, reaction_smi)
    all_mol.append(mol)
all_mol_tuple = tuple(all_mol)