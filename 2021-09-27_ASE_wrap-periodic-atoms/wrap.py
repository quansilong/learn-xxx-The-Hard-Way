
import numpy as np
from ase import Atoms, atom

def wrap_periodic(atoms:Atoms):
    "maybe only can be used for orthogonal"
    cell = atoms.cell.cellpar()
    assert cell[3] == 90
    assert cell[4] == 90
    assert cell[5] == 90
    assert any(atoms.pbc) #任意一真则为真
    _positions = []
    for atom in atoms:
        pos = atom.position
        assert all(pos >= 0)
        for i in range(3):
            coord = pos[i]
            coord_max = 0.5*cell[i]
            if coord > coord_max:
                pos[i] -= cell[i]
            assert np.abs(pos[i]) < coord_max
        _positions.append(pos)
    atoms.set_positions(_positions)
    return atoms



from ase.io import read, write
np.set_printoptions(precision=5)
np.set_printoptions(suppress=True)


atoms = read('CONTCAR')
print(atoms.positions)
atoms.wrap(pretty_translation=True)
print(atoms.positions)
atoms = wrap_periodic(atoms)
print(atoms.positions)
atoms.write('aaa.xyz')        
