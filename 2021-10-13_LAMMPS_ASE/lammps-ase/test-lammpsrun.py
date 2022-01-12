#!/usr/bin/env python3

import os, wget
from ase import Atom, Atoms
from ase.build import bulk
from ase.calculators.lammpsrun import LAMMPS    #基于文件的ASE计算器
from ase.calculators.lammpslib import LAMMPSlib #基于LAMMPS原生的Python接口

# 势函数下载
url = "https://openkim.org/files/MO_418978237058_005/NiAlH_jea.eam.alloy"
pot_fname = wget.filename_from_url(url)
if not os.path.exists(pot_fname):
    pot_fname = wget.download(url)


# 模型构建
Ni = bulk('Ni', cubic=True)
H = Atom('H', position=Ni.cell.diagonal()/2)
NiH = Ni + H
NiH.pbc = True

# 开始计算
lammps = LAMMPS(
    files       = [ pot_fname ], 
    parameters  = {
        'pair_style': 'eam/alloy',
        'pair_coeff': ['* * {} H Ni'.format(pot_fname)]})
lammps.set(command="/usr/bin/lmp")

NiH.calc = lammps
print("Energy ", NiH.get_potential_energy())