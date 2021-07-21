#naming_pattern_checks.py

import os

def run_namecheck_series():
	for file in os.listdir('working'):
		namecheck_chars(file)
		namecheck_underscores(file)
		namecheck_hyphen(file)
	print('checks_completed, proceede to packaging!')

def namecheck_chars(filepath):
	characters_disallowed = ['“', '~', '/', '?', '#', '[', ']', '@', '!', '$', '&','(', ')', '*', '+', ',', ';', '=', '{', '}', '|','\\', '^', '~', '‘', '"']
	for path in filepath:
		for c in characters_disallowed:
			if c in path:
				print('bad characters "' + c + '"  in ' + filepath)

def namecheck_underscores(filepath):
	chunks = filepath.split('_')
	if len(chunks) > 4:
		print('bad underscore in', filepath , 'too many underscores')
	if  len(chunks) < 1:
		print('No underscores in', filepath , 'where are my underscores?')


def namecheck_hyphen(filepath):
	chunks = filepath.split('-')
	if len(chunks) > 2:
		print('too many hypens in', filepath, 'only one hypen allowed to indicate sub-institutions')
		quit()

if __name__ == '__main__':
	run_namecheck_series()