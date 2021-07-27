#naming_pattern_checks.py

import os
import sys

def run_namecheck_series():
	error_counts = 0
	for file in os.listdir('working'):
		error_counts += namecheck_dots(file)
		error_counts += namecheck_chars(file)
		error_counts += namecheck_underscores(file)
		error_counts += namecheck_hyphen(file)
		error_counts += namecheck_lonely(file)
	print('checks_completed, proceeding to packaging!')
	return error_counts

def namecheck_dots(filepath):
	if filepath.count('.') > 1:
		print('too many periods "." in ' + filepath)
		return 1
	else:
		return 0

#does this need to loop at all
def namecheck_chars(filepath):
	bad_chars = 0
	characters_disallowed = ['“', '~', '/', '?', '#', '[', ']', '@', '!', '$', '&','(', ')', '*', '+', ',', ';', '=', '{', '}', '|','\\', '^', '~', '‘', '"']
	for c in characters_disallowed:
		if c in filepath:
			print('bad characters "' + c + '"  in ' + filepath)
			bad_chars += 1
	return bad_chars

def namecheck_underscores(filepath):
	bad_unders = 0
	chunks = filepath.split('_')
	if len(chunks) > 4:
		print('underscore count to large (3 max) in ' + filepath )
		bad_unders += 1
	if  len(chunks) < 1:
		print('underscores missing in ' + filepath)
		bad_unders += 1
	return bad_unders

def namecheck_hyphen(filepath):
	bad_hyphs = 0
	chunks = filepath.split('-')
	if len(chunks) > 1:
		print('hyphen limit (max 1) in ' + filepath )
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
		print('lonely object ' + filepath + "missing children if compound, or missing pair if simple")
		bad_lonesome += 1
	return bad_lonesome

if __name__ == '__main__':
	result = run_namecheck_series()
	sys.exit(result)


#separate checks for simples copy this and rename for simples 
#coupling of parentname within childname 
