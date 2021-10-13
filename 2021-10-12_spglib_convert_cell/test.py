from ase.build import bulk
from ase.io import read, write

test = bulk('Pd', 'fcc', 3.5, cubic=True)
write('POSCAR', test, format='vasp')


from convert import recell
recell(to_pricell=True)