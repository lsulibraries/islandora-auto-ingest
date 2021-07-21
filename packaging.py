#python script for organizing for ingest into LDL based on organize.py used for HNOC ingest in feb 2021
import os, shutil, sys
"""

simple objects should be output in a flat directory.

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
			os.rename('working/' + line, 'output/'+ending[0]+'/MODS.xml')


	#make subdirs loop
	for line in dirlist:
		#compound child identifier
		pattern = line.split('_')
		if len(pattern) > 3 and '.xml' in line:
			pattern.pop()
			folder = '_'.join(pattern)
			ending = line.split('.')
			os.makedirs('output/'+folder+'/'+line[:-4])

	#move children to subdirs loop
	for line in dirlist:
		#compound child identifier
		pattern = line.split('_')
		if len(pattern) > 3:
			pattern.pop()
			folder = '_'.join(pattern)
			ending = line.split('.')
			if '.xml' not in line:
				os.rename('working/' + line, 'output/'+folder+'/'+ending[0]+'/OBJ.'+ending[1])
			else:
				os.rename('working/' + line, 'output/'+folder+'/'+ending[0]+'/MODS.xml')

	print('files packaged into directory "output"')
	return 0

if __name__ == '__main__':
	result = package_compound_files()
	sys.exit(result)