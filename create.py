import os
from pymatgen.core import Structure
from pymatgen.io.vasp.sets import MPRelaxSet

listA = ['Ba','La','Pr','Sm','Sr']
listB1 = ['Co','Fe']#,'Co','Fe','Ni','Cu']
listB2 = ['Al','As','Bi','Ca','Ce','Cr','Dy','Er','Ga','Ge','Gd','Hf','In','Lu','Mg','Mo','Nb','Pb','Sb','Sc','Sm','Sn','Ta','Te','Ti','V','Y','Yb','Zn','Zr','p']# no W_pv
POS = {1:[16],2:[16,31],3:[16,22,23],4:[16,22,23,25],5:[16,21,22,23,25],6:[16,18,19,21,24,26],7:[16,18,19,21,23,24,26],8:[16,18,19,21,23,24,26,29]}
incar_set = {'ENCUT':400, 'ISMEAR':0, 'ISPIN':2, 'PREC':'Normal', 'NCORE':24}
kpoints_set = {'reciprocal_density':800}



for index1 in range(len(listB1)):
	os.chdir('./%s/' % listB1[index1])
	for index2 in range(len(listB2)):
		os.chdir('./%s/' %listB2[index2])
		if os.path.exists('1'):
			for index3 in range(1,9):
				os.chdir('./%d/' % index3)
				if not os.path.exists('INCAR'):
					S = Structure.from_file('POSCAR')
					Relax = MPRelaxSet(S, user_incar_settings = incar_set, user_kpoints_settings = kpoints_set)
					Relax.write_input('.')
				os.chdir('./../')
		else:
			if not os.path.exists('INCAR'):
				S = Structure.from_file('POSCAR')
				Relax = MPRelaxSet(S, user_incar_settings = incar_set, user_kpoints_settings = kpoints_set)
				Relax.write_input('.')
		os.chdir('./../')
	os.chdir('./../')

#structure = Structure.from_file('POSCAR')

#Relax = MPRelaxSet(structure=structure)
#Relax.write_input('examples/relax')

#incar_set = {'ENCUT':400, 'ISMEAR':0, 'ISPIN':1, 'PREC':'Normal', 'NCORE':24}
#kpoints_set = {'reciprocal_density':800}
#Relax = MPRelaxSet(structure, user_incar_settings = incar_set, user_kpoints_settings = kpoints_set)
#Relax.write_input('.')
