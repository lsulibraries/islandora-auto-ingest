#compound_drush_cmd.py

# if appropriately named a single file can derive the command
import os
cmodel_dict = { 'pdf':'sp_pdf','jp2':'sp_large_image_cmodel','mp4':'sp_videoCModel','mp3':'sp-audoCmodel'}
paths = os.walk('output')

#make this work for all extensions of OBJ files in case(future plans)
subfolder = []
extensions = []
for directory, subfolders, files in paths:
	subfolder.append(subfolders)
	for file in files:
		if 'OBJ' in file:
			ext = file.split('.')
			extensions.append(ext[1])
extensions = set(extensions)

big_cmodel_string = ''
for ext in extensions:
	big_cmodel_string += "islandora:{},".format(cmodel_dict[ext])

folder = subfolder[1]
chunks = folder[0]
chunks = chunks.split('_')

ns = chunks[0] + '-' + chunks[1]
namespace =' --namespace={} '.format(ns)
parent = '--parent={}:collection '.format(ns)
cModel = "--content_models={} ".format(big_cmodel_string)
target_type = "--target=/etc/islandora-auto-ingest-kit/output/ --type=directory "
cmd = "drush -u 1 icbsp " + cModel + target_type + parent + namespace

print(cmd)