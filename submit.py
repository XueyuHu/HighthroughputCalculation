import os

listA = ['Ba','La','Pr','Sm','Sr']
listB1 = ['Co','Fe'] #['Mn','Co','Fe','Ni','Cu']
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
				if os.path.exists('run.pbs'):
					os.system('rm run.pbs')
				os.system('cp ~/run.pbs .')
				f = open('run.pbs','r+')
				a = f.readlines()
				a[1] = '#PBS -N %s%s%d\n' %(listB1[index1],listB2[index2],index3)
				if listB2[index2] == 'Gd' or listB2[index2] == 'In' or listB2[index2] == 'Pb':
					a[5] = '#PBS -l walltime=24:00:00\n'
				f = open('run.pbs','w+')
				f.writelines(a)
				f.close()
				os.system('qsub run.pbs')
				os.chdir('./../')
		else:
			if os.path.exists('run.pbs'):
				os.system('rm run.pbs')
			os.system('cp ~/run.pbs .')
			f = open('run.pbs','r+')
			a = f.readlines()
			a[1] = '#PBS -N %s%s\n' %(listB1[index1],listB2[index2])
			f = open('run.pbs','w+')
			f.writelines(a)
			f.close()
			os.system('qsub run.pbs')
		os.chdir('./../')
	os.chdir('./../')

