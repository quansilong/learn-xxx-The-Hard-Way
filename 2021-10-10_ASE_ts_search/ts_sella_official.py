#!/usr/bin/env python3

import sys, os
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from sella import Sella, Constraints

# Set up your system as an ASE atoms object
slab = fcc111('Cu', (5, 5, 6), vacuum=7.5)
add_adsorbate(slab, 'Cu', 2.0, 'bridge')

# Optionally, create and populate a Constraints object.
cons = Constraints(slab)
for atom in slab:
    if atom.position[2] < slab.cell[2, 2] / 2.:
        cons.fix_translation(atom.index)

# Set up your calculator
slab.calc = EMT()

# Set up a Sella Dynamics object
py_fname = os.path.splitext(sys.argv[0])[0]
dyn = Sella(
    slab,
    constraints=cons,
    trajectory='{}.traj'.format(py_fname),
)

dyn.run(1e-3, 1000)
