import os
import sys


def run_namecheck_series():
    error_counts = 0
    for file in os.listdir('working'):
        # check for correct number of '.' in filename
        error_counts += namecheck_dots(file)
        if error_counts == 0:
            error_counts += namecheck_ext(file)
            error_counts += namecheck_object_pair(file)
        error_counts += namecheck_hyphen(file)
        error_counts += namecheck_underscores(file)
        error_counts += namecheck_chars(file)
        if error_counts == 0:
            error_counts += namecheck_lonely(file)
    if error_counts == 0:
        print("checks_completed, proceede to packaging")
    else:
        print("errors found {} total".format(error_counts))
    return error_counts


def namecheck_object_pair(filepath):
    filelist = os.listdir('working')
    splitpath = filepath.split('.')
    # only check object files for pairity, limit of 2 files sharing namepattern
    if splitpath[1] != 'xml':
        namepattern = splitpath[0]
        count = len(list(filter(lambda x: namepattern in x, filelist)))
        if count > 2:
            print('check file {}'.format(filepath))
            print('check pattern {}'.format(namepattern))
            print('more than two files share a filename'
                  ' correct the filenames')
            return 1
        else:
            # look for xml file that shares the namepattern
            namepattern += '{}'.format('.xml')
            if namepattern not in filelist:
                print('Object file {} is missing an xml file'.format(filepath))
                return 1
    return 0


def namecheck_ext(filepath):
    allowed_ext = ['pdf', 'jp2', 'mp4', 'mp3', 'xml']
    splitpath = filepath.split('.')
    if splitpath[1] not in allowed_ext:
        print("{} filetype unsupported".format(filepath))
        print("filetypes allowed:", allowed_ext)
        return 1
    else:
        return 0


def namecheck_dots(filepath):
    if filepath.count('.') > 1:
        print("too many periods '.' in {}".format(filepath))
        return 1
    elif filepath.count('.') == 0:
        print("there must be one dot/period character the filepath")
        return 1
    else:
        return 0


def namecheck_chars(filepath):
    bad_chars = 0
    disallowed = ['“~/?#[]@!$&()*+,;=}{|\\^~‘"']
    for c in disallowed:
        if c in filepath:
            print("bad characters '{0}' in {1}".format(c, filepath))
            bad_chars += 1
    return bad_chars


def namecheck_underscores(filepath):
    bad_unders = 0
    chunks = filepath.split('_')
    if len(chunks) > 4:
        print("underscore count to large (3 max) in {}".format(filepath))
        bad_unders += 1
    if len(chunks) < 3:
        print("underscores missing in {}".format(filepath))
        bad_unders += 1
    return bad_unders


def namecheck_hyphen(filepath):
    bad_hyphs = 0
    chunks = filepath.split('-')
    if len(chunks) > 2:
        print("hyphen limit (max 1) in {}".format(filepath))
        bad_hyphs += 1
    return bad_hyphs


def namecheck_lonely(filepath):
    bad_lonesome = 0
    filelist = os.listdir('working')
    name = filepath.split('.')
    count = len(list(filter(lambda x: name[0] in x, filelist)))
    if count <= 1:
        lonely_message = "lonely object {} missing pair or missing children"
        print(lonely_message.format(filepath))
        bad_lonesome += 1
    return bad_lonesome


if __name__ == '__main__':
    result = run_namecheck_series()
    sys.exit(result)
