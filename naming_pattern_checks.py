#naming_pattern_checks.py

#at this stage one zipfile has been moved into output
#a report.txt file exists with info about the file before and after checksums, date of process run.

import os
import zipfile 
import time


def die_or_continue_checkpid():
	#terminate if self or sibling auto-ingest process is already running. ()
	#os.
	condition = False
	if condition:
		die()
	else:
		for file in os.listdir('.'):
			if file.endswith('.txt'):
				file = file[7:-4]
				unzip_file()
				confirm_flat_dir()
				write_to_log('start-checks ', file, ' start naming_pattern_checks\n')
				run_namecheck_series()

				write_to_log('finish-checks', file, ' server_preprocessing.py process finished at {}\n'.format(time.time()))


def write_to_log(log_type, path, data):
		with open(path, 'a') as f:
			f.write(log_type + ' ' + data + '\n')

def unzip_file():
	files = os.listdir('output/')
	os.mkdir('output/flat_dir')
	for file in files:
		if '.zip' in file:
			try:
				with zipfile.ZipFile('output/{}'.format(file)) as z:
					z.extractall('output/flat_dir/')
					print("unzipped")
			except:
				print("invalid file")

def confirm_flat_dir():
	#confirm directory is flat
	for file in os.listdir('output/flat_dir'):
		if os.path.isdir(file):
			print("directory output/flat_dir is not flat flatten directory")
			#flatten_dir('output/flat_dir')
			flatten_dir(file)

def flatten_dir(directory_path):
	#for any folder in 'output/flad_dir':
	for file in os.listdir('output/flat_dir/{}'.format(directory_path)):
		print(file)
		if os.isdir(file):
			for f in os.listdir(file):
				print(f)
				os.move(f, 'output/flat_dir/')


def run_namecheck_series():
	for file in os.listdir('output/flat_dir'):
		file = 'output/flat_dir/{}'.format(file)
		print(file)
		namecheck_chars(file)
		namecheck_underscores(file)
		namecheck_hyphen(file)
		namecheck_counts(file)
		namecheck_pairs(file)


def namecheck_chars(filepath):
	characters_disallowed = ['“', '~', '/', '?', '#', '[', ']', '@', '!', '$', '&','(', ')', '*', '+', ',', ';', '=', '{', '}', '|','\\', '^', '~', '‘', '"']
	for path in filepath:
		for c in characters_disallowed:
			if c in path:
				print('bad characters in filenames')
				print(c)
				print(path)
				#ideally log all failures but complete process.


def namecheck_underscores(filepath):
	chunks = filepath.split('_')
	if len(chunks) > 3:
		write_to_log('bad underscore in', filepath , 'too many underscores')

def namecheck_hyphen(filepath):
	chunks = filepath.split('-')
	if len(chunks) > 2:
		write_to_log('too many hypens in', filepath, 'only one hypen allowed to indicate sub-institutions')


def namecheck_counts(filepath):
	print(os.listdir(filepath))
	#sort and count how many files are compound parent,
	#compound child
	#simple object


def namecheck_pairs(filepath):
	#confirm every pair is named the same
	for file in filepath:
		print(file)


if __name__ == '__main__':
	die_or_continue_checkpid()