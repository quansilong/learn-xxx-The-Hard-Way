#!/usr/bin/env python3

import sys, os
from ase.build import molecule
from ase import Atom, Atoms
from ase.calculators.emt import EMT
from ase.optimize import QuasiNewton, MDMin
from ase.optimize.fire import FIRE
from ase.neb import NEB, NEBTools
from ase.io import iread


# Optimise molecule.
initial = molecule('C2H6')
initial.calc = EMT()
relax = QuasiNewton(initial)
relax.run(fmax=0.05)
# Create final state.
final = initial.copy()
final.positions[2:5] = initial.positions[[3, 4, 2]]
# Generate blank images.
images = [initial]
for i in range(9):
    images.append(initial.copy())
for image in images:
    image.calc = EMT()
images.append(final)



neb = NEB(images, climb=True)
neb.interpolate(method='idpp') #idpp插值，设置初猜

# set calculator
for atoms in images:
    atoms.calc = EMT()
    atoms.get_potential_energy()

# Optimize:
py_fname   = os.path.splitext(sys.argv[0])[0]
traj_fname = "{}.traj".format(py_fname)
log_fname  = "{}.log".format(py_fname)
optimizer = FIRE(neb, trajectory=traj_fname, logfile=log_fname)
optimizer.run(fmax=0.04)



neb_result = list(iread(traj_fname))
for i in neb_result:
    #print(i.get_potential_energy())
    pass
neb_result = NEBTools(neb_result)
neb_result.plot_bands(True, True, label=py_fname)
print(neb_result.get_barrier(), neb_result.get_fmax())