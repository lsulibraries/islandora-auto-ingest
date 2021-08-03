import os
import sys


def run_namecheck_series():
    error_counts = 0
    for file in os.listdir('working'):
        error_counts += namecheck_dots(file)
        if error_counts == 0:
            error_counts += namecheck_ext(file)
            error_counts += namecheck_has_xml(file)
            error_counts += namecheck_dupe_obj(file)
        error_counts += namecheck_chars(file)
        if error_counts == 0:
            error_counts += namecheck_lonely(file)
        error_counts += namecheck_underscores(file)
        error_counts += namecheck_hyphen(file)
    if error_counts == 0:
        print("checks_completed, proceede to packaging")
    else:
        print("errors found {} total".format(error_counts))
    return error_counts


def namecheck_has_xml(filepath):
    filelist = os.listdir('working')
    splitpath = filepath.split('.')
    if splitpath[1] != 'xml':
        pair = splitpath[0]
        pair += '{}'.format('.xml')
        if pair not in filelist:
            print('Object file {} is missing an xml file'.format(filepath))
            return 1
        else:
            return 0
    else:
        return 0


def namecheck_dupe_obj(filepath):
    if '.xml' not in filepath:
        filelist = os.listdir('working')
        splitpath = filepath.split('.')
        count = 0
        for file in filelist:
            if splitpath[0] in file:
                count += 1
        if count < 3:
            return 0
        else:
            print('check file {}'.format(filepath))
            print('check pattern {}'.format(splitpath[0]))
            print('more than two files share a filename, '
                  'naming pattern expects a '
                  'mods-object pair, not a trio or more')
            return 1
    else:
        return 0


def namecheck_ext(filepath):
    allowed_ext = ['pdf', 'jp2', 'mp4', 'mp3', 'xml']
    splitpath = filepath.split('.')
    if splitpath[1] not in allowed_ext:
        print("{} filetype unsupported".format(filepath))
        print("filetypes unsupported:", allowed_ext)
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
    characters_disallowed = ['“~/?#[]@!$&()*+,;=}{|\\^~‘"']
    for c in characters_disallowed:
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
    count = 0
    chunks = filepath.split('.')
    for file in os.listdir('working'):
        if chunks[0] in file:
            count += 1
    if count <= 1:
        lonely_message = "lonely object {} missing pair or missing children"
        print(lonely_message.format(filepath))
        bad_lonesome += 1
    return bad_lonesome


if __name__ == '__main__':
    result = run_namecheck_series()
    sys.exit(result)
