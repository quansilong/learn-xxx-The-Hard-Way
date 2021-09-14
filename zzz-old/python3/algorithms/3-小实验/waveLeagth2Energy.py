from scipy import constants as fcp

print("")
print("==" *30)
wave_length = input('Please input the wavelength(nm):')
                    
energy_one = fcp.h * fcp.c  * 1e9 / float(wave_length)
energy_mol = energy_one * fcp.N_A
      
print()
print("The energy of one photon is :", energy_one, "J" )
print("The energy of one photon is :", energy_one / fcp.electron_volt, "eV" )
print("The energy of one mol photon is :", energy_mol / 1e-3, "kJ/mol" )
print("==" *30)