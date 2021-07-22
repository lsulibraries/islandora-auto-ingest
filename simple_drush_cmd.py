#simple_drush_cmd.py

import os
cmodel_dict = { 'pdf':'sp_pdf','jp2':'sp_large_image_cmodel','mp4':'sp_videoCModel','mp3':'sp-audoCmodel'}
paths = os.listdir('output')


#check for dirs if dirs quit
one_path_is_all = ''
for path in paths:
	if '.xml' not in path:
		one_path_is_all = path

objtype = one_path_is_all.split('.')
chunks = one_path_is_all.split('_')

ns = chunks[0] + '-' + chunks[1]
namespace = '--namespace={} '.format(ns)
parent = ns + ':collection'
cModel = "--content_models=islandora:{} ".format(cmodel_dict[objtype[1]])
target_type = "--target=/etc/islandora-auto-ingest-kit/output/ --type=directory "
cmd = "drush -u 1 ibsp " + cModel + target_type + parent + namespace
print(cmd)