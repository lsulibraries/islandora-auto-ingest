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
import os
import sys


def package_compound_files():
    dirlist = os.listdir('working/')
    for line in dirlist:
        pattern = line.split('_')
        ending = line.split('.')
        # compound parent identifier
        if '.xml' in line and len(pattern) == 3:
            os.makedirs("output/{}".format(ending[0]))
            source = "working/{}".format(line)
            dest = "output/{}/MODS.xml".format(ending[0])
            os.rename(source, dest)
    for line in dirlist:
        # compound child identifier
        pattern = line.split('_')
        if len(pattern) > 3 and '.xml' in line:
            pattern.pop()
            subdir = '_'.join(pattern)
            ending = line.split('.')
            path = "output/{0}/{1}".format(subdir, ending[0])
            print(path)
            os.makedirs(path)
    # move children to subdirs loop
    for line in dirlist:
        # compound child identifier
        pattern = line.split('_')
        if len(pattern) > 3:
            pattern.pop()
            foldr = '_'.join(pattern)
            end = line.split('.')
            if '.xml' not in line:
                source = "working/{}".format(line)
                dest = "output/{0}/{1}/OBJ.{2}".format(foldr, end[0], end[1])
                os.rename(source, dest)
            else:
                source = "working/{}".format(line)
                dest_string = "output/{0}/{1}/MODS.xml"
                dest = dest_string.format(foldr, end[0])
                os.rename(source, dest)
    print("files packaged into directory 'output'")
    return 0


if __name__ == '__main__':
    result = package_compound_files()
    sys.exit(result)
