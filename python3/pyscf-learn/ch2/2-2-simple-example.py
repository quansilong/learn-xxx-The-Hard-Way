from pyscf import gto,scf

mol = gto.M(atom = "H 0 0 0; H 0 0 1.2", basis = 'ccpvdz')
mf = scf.RHF(mol)
mf.kernel()
# Output:
#    converged SCF energy = -1.06111199785749

