#!/usr/bin/env python3

import sys, os
from ase import Atom, Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import QuasiNewton
from sella import Sella, Constraints

# Set up your system as an ASE atoms object
test = Atoms( [ Atom('Cu',[0,0,0]),
                Atom('Cu',[3,0,0]),
                Atom('Cu',[0,3,0]) ])
test.set_cell([20,20,20])
test.set_pbc(True)

# Optionally, create and populate a Constraints object.
#cons = Constraints(slab)
#for atom in slab:
#    if atom.position[2] < slab.cell[2, 2] / 2.:
#        cons.fix_translation(atom.index)

# Set up your calculator
test.calc = EMT()


# Optimize system
#opt = QuasiNewton(test)
#opt.run()


# Set up a Sella Dynamics object
py_fname = os.path.splitext(sys.argv[0])[0]
dyn = Sella(
    test,
    #constraints=cons,
    trajectory='{}.traj'.format(py_fname),
)

dyn.run(1e-3, 1000)
