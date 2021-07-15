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
				print('bad characters in filenames')
				print(c)
				print(path)

def namecheck_underscores(filepath):
	chunks = filepath.split('_')
	if len(chunks) > 4:
		print('bad underscore in', filepath , 'too many underscores')
	if  len(chunks) < 1:
		print('No underscores in', filepath , 'do you even naming convention?')

		#write_to_log('bad underscore in', filepath , 'too many underscores')

def namecheck_hyphen(filepath):
	chunks = filepath.split('-')
	if len(chunks) > 2:
		print('too many hypens in', filepath, 'only one hypen allowed to indicate sub-institutions')
		#write_to_log('too many hypens in', filepath, 'only one hypen allowed to indicate sub-institutions')
		quit()

if __name__ == '__main__':
	confirm_flat_dir()
	run_namecheck_series()