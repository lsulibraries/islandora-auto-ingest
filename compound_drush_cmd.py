#compound_drush_cmd.py

# if appropriately named a single file can derive the command
import os, sys

def compound_command_populator():
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
		if ext in cmodel_dict:
			big_cmodel_string += "islandora:{},".format(cmodel_dict[ext])
		else:
			print('filetype not supported for packaging')
			return 1

	folder = subfolder[1]
	chunks = folder[0]
	chunks = chunks.split('_')

	ns = chunks[0] + '-' + chunks[1]
	namespace ='--namespace={}'.format(ns)
	parent = '--parent={}:collection'.format(ns)
	cModel = "--content_models={}".format(big_cmodel_string)
	target_type = "--target=/etc/islandora-auto-ingest-kit/output/ --type=directory "
	cmd = "drush -u 1 icbsp {0} {1} {2} {3}".format(cModel, target_type, parent, namespace)
	print('constructed drush command for execution, review args for accuracy:', cmd)
	return 0

if __name__ == '__main__':
	status = compound_command_populator()
	sys.exit(status)