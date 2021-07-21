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

#with naming convention as is, it is difficult to tell if a simple object is a compound parent.
dirlist = os.listdir('working/')

for line in dirlist:
	pattern = line.split('_')
	#compound parent identifier (cannot tell difference between simple)
	if '.xml' in line and len(pattern) == 3:
		os.makedirs('output/'+line[:-4])
		os.rename('working/' + line, 'output/'+line[:-4]+'/MODS.xml')

#make subdirs loop
for line in dirlist:
	#compound child identifier
	pattern = line.split('_')
	if len(pattern) > 3 and '.xml' in line:
		ending = line.split('.')
		os.makedirs('output/'+line[:-8]+'/'+line[:-4])

#move children to subdirs loop
for line in dirlist:
	#compound child identifier
	pattern = line.split('_')
	if len(pattern) > 3:
		ending = line.split('.')
		if '.xml' not in line:
			os.rename('working/' + line, 'output/'+line[:-8]+'/'+line[:-4]+'/OBJ.'+ending[1])
		else:
			os.rename('working/' + line, 'output/'+line[:-8]+'/'+line[:-4]+'/MODS.xml')

print('files packaged into directory "output"')