#Having the initial POSCAR, this script dopes the structure and creates the new POSCAR

import os
from pymatgen.core import Structure

S = Structure.from_file('POSCAR')

listA = ['Ba','La','Pr','Sm','Sr']
listB1 = ['Co','Fe']#,'Fe','Ni','Cu']
listB2 = ['Al','As','Bi','Ca','Ce','Cr','Dy','Er','Ga','Ge','Gd','Hf','In','Lu','Mg','Mo','Nb','Pb','Sb','Sc','Sm','Sn','Ta','Te','Ti','V','Y','Yb','Zn','Zr']
POS = {1:[16],2:[16,31],3:[16,22,23],4:[16,22,23,25],5:[16,21,22,23,25],6:[16,18,19,21,24,26],7:[16,18,19,21,23,24,26],8:[16,18,19,21,23,24,26,29]}

for index1 in range(len(listB1)):
	for j in range(16,32):
		S.replace(i=j, species = listB1[index1])
	if not os.path.exists('./%s/p/' % listB1[index1]):
		os.makedirs('./%s/p/' % listB1[index1])
	S.to(filename = './%s/p/POSCAR' % listB1[index1], fmt = 'poscar')
	for index2 in range(len(listB2)):
		for index3 in range(1,9):
			s = Structure.from_file('./%s/p/POSCAR' % listB1[index1])
			for index4 in range(len(POS[index3])):
				s.replace(i=POS[index3][index4], species = listB2[index2])
			if not os.path.exists('./%s/%s/%d/' % (listB1[index1],listB2[index2],index3)):
				os.makedirs('./%s/%s/%d/' % (listB1[index1],listB2[index2],index3))
			s.to(filename = './%s/%s/%d/POSCAR' % (listB1[index1],listB2[index2],index3), fmt = 'poscar')
