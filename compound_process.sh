#!/bin/bash
unzip input/* -d  working
python3 naming_pattern_checks.py
if [ $? -eq 0 ] 
then
	python3 packaging.py
	if [ $? -eq 0 ] 
	then
		#cd /var/www/drupal7/sites/all/modules/islandora_compound_batch/extras/scripts
		cd /Users/kcome26/islandora_compound_batch/extras/scripts
		#php create_structure_files.php /etc/islandora-auto-ingest/output/
		php create_structure_files.php /Users/kcome26/islandora-auto-ingest-kit/output
		echo 'packaged and structured'
	fi
else
	echo 'check files for naming patterns, packaging canceled'
fi
python3 compound_drush_cmd.py
