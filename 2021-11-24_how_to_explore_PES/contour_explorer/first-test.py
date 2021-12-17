#!/usr/bin/env python3
# paper:        https://arxiv.org/abs/2103.08054 
# document:     https://wiki.fysik.dtu.dk/ase/ase/md.html
# source code:  https://wiki.fysik.dtu.dk/ase/_modules/ase/md/contour_exploration.html#ContourExploration

from ase.md.contour_exploration import ContourExploration as Contour
from ase.build import bulk, molecule, add_vacuum
from ase.calculators.emt import EMT

# 1. perform contour exploration
#atoms = molecule("CH3CH2OH")
atoms = bulk("Pd" , "fcc", 3.5, cubic=True)
atoms *= (4,4,2)
add_vacuum(atoms, 10)
atoms.pbc = True
atoms.calc = EMT()
#test = Contour(atoms,
#    energy_target=None,
#    remove_translation=True,
#    logfile='-',
#    trajectory="a.traj"
#    )
#test.run(1000)

# 2. wrap atoms
from ase.io import read, iread
from ase.io.trajectory import Trajectory
def wrap_traj(ofname, nfname):
    traj = Trajectory(nfname, "w")
    for frame in iread(ofname):
        frame.wrap()
        traj.write(frame,)
wrap_traj("a.traj", "b.traj")

