#python script for organizing for ingest into LDL based on organize.py used for HNOC ingest in feb 2021
import os, shutil
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
dirlist = os.listdir('working/')
print(dirlist)
os.makedirs('output/simple')
os.makedirs('output/compound')

for line in dirlist:
	path = 'working/' + line
	if os.path.isdir(path):
	#compound condition
		print(path.strip())
		if len(path.split('_')) > 2 and len(path.split('_')) < 3:
			somewhere="output/compound/{}".format(line.strip())
			meta_dest = somewhere + '/' + 'MODS.xml'
		if '.xml' not in line:
			os.makedirs(somewhere+'/'+line[:-4])
			os.rename(path, somewhere+'/'+line[:-4]+'/'+'OBJ.jp2')
			shutil.copyfile('output/compound/'+line[:-4]+'.xml', somewhere+'/'+line[:-4]+'/MODS.xml')

			os.rename("{}.xml".format(compound_meta), meta_dest)
	else:
		dest = 'output/simple/{}'.format(line.strip())
		#move to simple folder
		shutil.move(path, dest)
