#naming_pattern_checks.py

#at this stage one zipfile has been moved into output
#a report.txt file exists with info about the file before and after checksums, date of process run.

import os
import zipfile 
#import time


# def die_or_continue_checkpid():
# 	#terminate if self or sibling auto-ingest process is already running. ()
# 	#os.
# 	condition = False
# 	if condition:
# 		die()
# 	else:
# 		for file in os.listdir('.'):
# 			if file.endswith('.txt'):
# 				file = file[7:-4]
# 				unzip_file()
# 				confirm_flat_dir()
# 				write_to_log('start-checks ', file, ' start naming_pattern_checks\n')
# 				run_namecheck_series()

# 				write_to_log('finish-checks', file, ' server_preprocessing.py process finished at {}\n'.format(time.time()))


# def write_to_log(log_type, path, data):
# 		with open(path, 'a') as f:
# 			f.write(log_type + ' ' + data + '\n')

def unzip_file():
	files = os.listdir('input/')
	for file in files:
		if '.zip' in file:
			try:
				with zipfile.ZipFile('input/{}'.format(file)) as z:
					z.extractall('working/')
					print("unzipped")
			except:
				print("invalid file")


def confirm_flat_dir():
	#confirm directory is flat
	for file in os.listdir('working/'):
		if os.path.isdir('working/{}'.format(file)):
			print("supplied files incorrectly packaged")
			flatten_dir('working/{}'.format(file))
		else:
			print('already flattened')


def flatten_dir(directory_path):
	#WIP
	#for any folder in 'output/flad_dir'
	all_files_in_dir = []
	for root, folders, file in os.walk(directory_path):

		# print(root)
		# print(folders)
		# print(file)
		if os.path.isdir(directory_path+'/{}'.format(file)):
			for f in os.listdir(file):
				if os.path.isdir(f):
					#print(directory_path+'/{}'.format(file)+'/{}'.format(f))
					os.move(directory_path+'/{}'.format(file)+'/{}'.format(f), 'output/')
	quit()



def run_namecheck_series():
	for file in os.listdir('working'):
		file = 'working/{}'.format(file)
		#print(file)
		#namecheck_chars(file)
		namecheck_underscores(file)
		namecheck_hyphen(file)
		#namecheck_counts(file)
		#namecheck_pairs(file)
	print('checks_completed, proceede to packaging!')


# def namecheck_chars(filepath):
# 	characters_disallowed = ['“', '~', '/', '?', '#', '[', ']', '@', '!', '$', '&','(', ')', '*', '+', ',', ';', '=', '{', '}', '|','\\', '^', '~', '‘', '"']
# 	for path in filepath:
# 		for c in characters_disallowed:
# 			if c in path:
# 				print('bad characters in filenames')
# 				print(c)
# 				print(path)
# 				#ideally log all failures but complete process.


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


# def namecheck_counts(filepath):
# 	print(os.listdir(filepath))
# 	#sort and count how many files are compound parent,
# 	#compound child
# 	#simple object


def namecheck_pairs(filepath):
	#confirm every pair is named the same
	for file in filepath:
		filename = file.split('.')
		print(file)


if __name__ == '__main__':
	#die_or_continue_checkpid()
	unzip_file()
	confirm_flat_dir()
	run_namecheck_series()
