#simple_drush_cmd.py

import os


def simple_command_populator():
	cmodel_dict = { 'pdf':'sp_pdf','jp2':'sp_large_image_cmodel','mp4':'sp_videoCModel','mp3':'sp-audoCmodel'}
	paths = os.listdir('output')


	#check for dirs if dirs quit
	one_path_is_all = ''
	for path in paths:
		if os.path.isdir(path):
			print('error, directory in output. this is not a simple object set')
			return 1
		if '.xml' not in path:
			one_path_is_all = path

	objtype = one_path_is_all.split('.')
	chunks = one_path_is_all.split('_')

	ns = '{0}-{1}'.format(chunks[0], chunks[1])
	namespace = '--namespace={} '.format(ns)
	parent = ns + ':collection'
	cModel = '--content_models=islandora:{} '.format(cmodel_dict[objtype[1]])
	target_type = '--target=/etc/islandora-auto-ingest-kit/output/ --type=directory '
	cmd = 'drush -u 1 ibsp {0} {1} {2} {3}'.format(cModel, target_type, parent, namespace)
	print('constructed drush command for execution, review args for accuracy:', cmd)
	return 0

if __name__ == '__main__':
	status = simple_command_populator()
	sys.exit(status)