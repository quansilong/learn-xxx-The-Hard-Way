#!/usr/bin/env python3
# paper:        https://arxiv.org/abs/2103.08054 
# document:     https://wiki.fysik.dtu.dk/ase/ase/md.html
# source code:  https://wiki.fysik.dtu.dk/ase/_modules/ase/md/contour_exploration.html#ContourExploration

from ase.md.contour_exploration import ContourExploration as Contour
from ase.build import molecule
from ase.calculators.emt import EMT


atoms = molecule("CH3CH2OH")
atoms.calc = EMT()
test = Contour(atoms,
    maxstep=0.5,        # 每次迭代中，原子的最大可移动距离
    parallel_drift=0.1, # 每次迭代中，与等高线平行但是方向随机的部分【用于打破对称性】
    energy_target=None, # 恒势能器尝试保持的系统目标势能，默认是初始构型的势能
    angle_limit=20,     # 使用曲率改变方向的最大角度
                        #       通常小于30度就可以给出合理的结果，
                        #       且角度越小恒势能的精度也越高，默认是20度
    potentiostat_step_scale=None,   # 恒势能器的步长缩放系数。
                        #       恒势能步长是由当前势能、目标势能和当前受力
                        #       线性外推得到的。该系数大于1.0会过矫正，而小于1.0会欠矫正。
                        #       默认情况下，会根据parallel_drift的值来调整这个数值。
    remove_translation=False,       #
    logfile='-',
    trajectory="a.traj"
    )
test.run(1000)
