import spglib
import numpy as np
import os
import linecache

class read_poscar(object):
    def __init__(
        self,
        struct=None,
        pos_name=None,
        lattice_index=None,
        lat=None,
        lat_recell=None,
        atomname=None,
        atomnum=None,
        postype=None,
        pos=None,
        spg_number=None,
    ):
        self.struct = linecache.getlines("POSCAR")
        # read POSCAR to get some paramatrics: sys_name; lattice; atom_name; atom_number; atom_position
        # and get spacegroup_number
        poscar = [line.strip() for line in self.struct]
        num = len(poscar)

        self.pos_name = poscar[0].split()
        self.lat_index = poscar[1].split()
        self.lattice_index = float(self.lat_index[0])

        # matrics of lattice vector

        lat_vector = np.zeros((3, 3))
        index = 0
        for latt in poscar[2:5]:
            latt = latt.split()
            lat_vector[index, :] = latt[0:3]
            index += 1
        self.lattice = lat_vector

        self.atomname = poscar[5].split()
        self.atomnum = poscar[6].split()
        self.postype = poscar[7].split()

        atom_len=len(self.atomname)

        # matrics of atom position

        i = num - 8
        position_vector = np.zeros((i, 3))
        index = 0
        for poss in poscar[8:num]:
            poss = poss.split()
            #position_vector[index, 0:3] = poss[0:3]
            position_vector[index,0] = poss[0]
            position_vector[index,1] = poss[1]
            position_vector[index,2] = poss[2]
            index += 1

        self.lat = lat_vector * self.lattice_index
        self.pos = position_vector
        atom_numbers = [1,] * (int(self.atomnum[0]))#+int(self.atomnum[1]))
        cell = (self.lat, self.pos, atom_numbers)
        database = spglib.get_symmetry_dataset(
            cell, symprec=1e-3
        )
        self.spg_number = database["number"]

    def system_name(self):
        return self.pos_name

    def latt_index(self):
        return self.lattice_index

    def latti(self):
        return self.lattice

    def atom_name(self):
        return self.atomname

    def atom_number(self):
        return self.atomnum

    def position_type(self):
        return self.postype

    def positions(self):
        return self.pos

    def spacegroup_num(self):
        return self.spg_number

'''来源: ZSaying
作者: ZSaying
链接: https://mixzeng.github.io/2020/12/27/crystal-cell-convert/#toc-heading-4
本文章著作权归作者所有，任何形式的转载都请注明出处。'''