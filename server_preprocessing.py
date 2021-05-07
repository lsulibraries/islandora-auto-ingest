#server_preprocessing.py


import os
import shutil
import hashlib
import time

def die_or_continue_checkpid():
	#terminate if self or sibling auto-ingest process is already running.
	condition = False
	if condition:
		die()
	else:

		file = first_zipfile_name()
		#
		copy_files(file)
		check_zipfile_hash_for_delta(file)
		write_to_log('finished', file, 'server_preprocessing.py finished at {}'.format(time.time()))


def first_zipfile_name():
	zip_list = os.listdir('input/') 
	return zip_list[0]

def copy_files(path):
	write_checksum('pre-transfer', path)
	write_to_log('zipfile', path, 'starting\n')
	shutil.copy('input/{}'.format(path), 'output/{}'.format(path))
	#eventually this is copying from box to server
	write_checksum('post-transfer', path)


def write_checksum(stage, path):
	if stage == 'pre-transfer':
		with open('input/{}'.format(path),'rb') as f:
			data = f.read()
			checksum = hashlib.sha256(data).hexdigest();
		write_to_log(stage, path, checksum)
	else:
		with open('output/{}'.format(path),'rb') as f:
			data = f.read()
			checksum = hashlib.sha256(data).hexdigest()
		write_to_log(stage, path, checksum)


def write_to_log(log_type, path, data):
	if log_type == 'pre-transfer':
		with open('report-{}.txt'.format(path[0:-4]), 'w') as f:
			f.write(log_type + ' ' + data + '\n')
	else:
		with open('report-{}.txt'.format(path[0:-4]), 'a') as f:
			f.write(log_type + ' ' + data + '\n')

def check_zipfile_hash_for_delta(path):
	sums = []
	with open('report-{}.txt'.format(path[0:-4]), 'r') as report:
		for line in report.readlines():
			if 'transfer' in line:
				log_parts = line.split(' ')
				sums.append(log_parts[1])
		if sums[0] == sums[1]:
			write_to_log('checksums match', path, 'good')
		else:
			write_to_log('checksums match', path, 'failed')
			die()
#if the checksums have changed, report

if __name__ == '__main__':
	die_or_continue_checkpid()

#copies files to server from box logs checksums before and after