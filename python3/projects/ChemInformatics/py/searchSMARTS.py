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
   

# 子结构搜索
def structureSearch(smarts_string, mol_name):
    molecule = pybel.readstring("smi", mol_name)
    smarts = pybel.Smarts(smarts_string)
    # print(smarts.findall(molecule))
    return smarts.findall(molecule)
    
# 搜索测试
F2 = []
for i3 in all_mol_tuple:
    #print(i3)
    #print()
    result = []
    for i in i3[1].split(">"):
        result.append(structureSearch("[F*]",i))
    if result[0]:
        if result[1]:
            if result[1]:
                #print(i3[0],result)
                F2.append(i3[0])
   #else:
    #    print("None result ")
print(len(F2))
# 验证搜索