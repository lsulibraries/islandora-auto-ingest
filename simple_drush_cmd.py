import os
import sys


def simple_command_populator():
    cmodel_dict = {'pdf': 'sp_pdf',
                   'jp2': 'sp_large_image_cmodel',
                   'mp4': 'sp_videoCModel',
                   'mp3': 'sp-audoCmodel'}
    paths = os.listdir('output')
    # check for dirs if dirs quit
    one_path_is_all = ''
    for path in paths:
        if os.path.isdir(path):
            print('error, directory in output.'
                  ' this is not a simple object set')
            return 1
        if '.xml' not in path:
            one_path_is_all = path

    objtype = one_path_is_all.split('.')
    chunks = one_path_is_all.split('_')
    ns = '{0}-{1}'.format(chunks[0], chunks[1])
    namespace = '--namespace={}'.format(ns)
    parent = "{}:collection".format(ns)
    cmodel_str = "--content_models=islandora:{}"
    cmodel = cmodel_str.format(cmodel_dict[objtype[1]])
    target = '--target=/etc/islandora-auto-ingest-kit/output/'
    target += ' --type=directory'
    cmd_str = 'drush -u 1 ibsp {0} {1} {2} {3}'
    cmd = cmd_str.format(cmodel, target, parent, namespace)
    print('constructed drush command for execution,'
          " review args for accuracy:\n", cmd)
    return 0


if __name__ == '__main__':
    status = simple_command_populator()
    sys.exit(status)
