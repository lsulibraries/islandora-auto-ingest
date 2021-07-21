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
		error_counts += namecheck_parent(file)

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
		print('bad underscore in', filepath , 'too many underscores')
		bad_unders += 1
	if  len(chunks) < 1:
		print('No underscores in', filepath , 'where are my underscores?')
		bad_unders += 1
	return bad_unders

def namecheck_hyphen(filepath):
	bad_hyphs = 0
	chunks = filepath.split('-')
	if len(chunks) > 2:
		print('too many hypens in', filepath, 'only one hypen allowed to indicate sub-institutions')
		bad_hyphs += 1
	return bad_hyphs

def namecheck_parent(filepath):
	bad_parents = 0
	count = 0
	chunks = filepath.split('.')
	for file in os.listdir('working'):
		if chunks[0] in file:
			count += 1
	if count <= 1:
		print('parent object ' + filepath + 'has no children, remove or add children')
		bad_parents += 1
	return bad_parents

if __name__ == '__main__':
	result = run_namecheck_series()
	sys.exit(result)


#separate checks for simples copy this and rename for simples 
#coupling of parentname within childname 
