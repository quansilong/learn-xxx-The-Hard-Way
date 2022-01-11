#!/usr/bin/env python3

from ase import Atom, Atoms
from ase.build import bulk, fcc100, add_adsorbate, add_vacuum
from ase.calculators.vasp import Vasp
from ase.calculators.kim.kim import KIM
from ase.calculators.qmmm import ForceQMMM, RescaledCalculator
from ase.constraints import StrainFilter
from ase.optimize import LBFGS
from ase.visualize import view

atoms = bulk("Pd", "fcc", a=3.5, cubic=True)
atoms.calc = KIM("MEAM_LAMMPS_JeongParkDo_2018_PdMo__MO_356501945107_000")
opt = LBFGS(StrainFilter(atoms), logfile=None)
opt.run(0.03, steps=30)
length = atoms.cell.cellpar()[0]

atoms = fcc100("Pd", (2,2,5), a=length, vacuum=10, periodic=True)
add_adsorbate(atoms, Atoms([Atom("Mo")]), 1.2)


qm_mask = [len(atoms)-1, len(atoms)-2]
qm_calc = Vasp(directory="./qmmm")
mm_calc = KIM("MEAM_LAMMPS_JeongParkDo_2018_PdMo__MO_356501945107_000")
mm_calc = RescaledCalculator(mm_calc, 1, 1, 1, 1)
qmmm = ForceQMMM(atoms, qm_mask, qm_calc, mm_calc, buffer_width=3)
qmmm.initialize_qm_buffer_mask(atoms)
atoms.pbc=True
atoms.calc = qmmm

print(atoms.get_forces())

