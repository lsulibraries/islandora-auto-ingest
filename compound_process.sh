#!/bin/bash
unzip -q -d  working input/*
python3 naming_pattern_checks.py
if [ $? -eq 0 ] 
then
	python3 packaging.py
	if [ $? -eq 0 ] 
	then
		cd /var/www/drupal7/sites/all/modules/islandora_compound_batch/extras/scripts
		#cd /home/wwc/Clones/islandora_compound_batch/extras/scripts
		php create_structure_files.php /etc/islandora-auto-ingest/output/
		#php create_structure_files.php /home/wwc/Clones/islandora-auto-ingest/output
		echo 'packaged and structured'
		cd /etc/islandora-auto-ingest
		python3 compound_drush_cmd.py
	else
		echo 'packaging failed, command population canceled'
	fi
else
	echo 'check files for naming patterns, packaging canceled'
fi
