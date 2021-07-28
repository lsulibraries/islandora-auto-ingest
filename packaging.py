#python script for organizing for ingest into LDL based on organize.py used for HNOC ingest in feb 2021
import os, sys
"""
Desired output for compound objects:

input_directory
├── parent_one
│   ├── first_child
│   │   ├── MODS.xml
│   │   └── OBJ.jp2
│   ├── second_child
│   │   ├── MODS.xml
│   │   └── OBJ.jp2
│   └── MODS.xml
│   
└── parent_two
	├── first_child
	│   ├── MODS.xml
	│   └── OBJ.jp2
	├── second_child
	│   ├── MODS.xml
	│   └── OBJ.jp2
	└── MODS.xml

"""

def package_compound_files():
#with naming convention as is, it is difficult to tell if a simple object is a compound parent.
	dirlist = os.listdir('working/')

	for line in dirlist:
		pattern = line.split('_')
		ending = line.split('.')
		#compound parent identifier (cannot tell difference between simple)
		if '.xml' in line and len(pattern) == 3:
			os.makedirs('output/'+ending[0])
			os.rename('working/{}'.format(line), 'output/{}/MODS.xml'.format(ending[0]))


	#make subdirs loop
	for line in dirlist:
		#compound child identifier
		pattern = line.split('_')
		if len(pattern) > 3 and '.xml' in line:
			pattern.pop()
			folder = '_'.join(pattern)
			ending = line.split('.')
			os.makedirs('output/{0}/{1}'.format(folder, ending[1]))

	#move children to subdirs loop
	for line in dirlist:
		#compound child identifier
		pattern = line.split('_')
		if len(pattern) > 3:
			pattern.pop()
			folder = '_'.join(pattern)
			ending = line.split('.')
			if '.xml' not in line:
				source = 'working/{}'.format(line)
				dest = 'output/{0}/{1}/OBJ.{2}'.format(folder, ending[0], ending[1])
				os.rename(source, dest )
			else:
				source ='working/{}'.format(line)
				dest = 'output/{0}/{1}/MODS.xml'.format(folder, ending[0])
				os.rename(source, dest)
	print('files packaged into directory "output"')
	return 0

if __name__ == '__main__':
	result = package_compound_files()
	sys.exit(result)