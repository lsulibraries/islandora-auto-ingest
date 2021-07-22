#ingest packager and nameconvention checker for louisiana digital library LDL

requirements, islandora_compound_batch module is needed for creating structure files
instructions for running the prototype:

open a terminal and navigate to the path of this git repository


initial setup: script to create some directories where files get placed and packaged:

- ```sh setup.sh```

copy your zipped files to the input folder
for example:

- ```cp ~/Downloads/yourfiles.zip input/```

simple object procedures 
this only checks the files for adherence to the naming patterns
- ```sh simpleprocess.sh```

compound object procedures
for compounds the files are checked for adherence to naming patterns and packaged appropriately
- ```sh compound_process.sh```


you files will be placed in the output directory after they are packaged. If they are compound, they can now be a target for the create_structure.php script that comes with the islandora_compound_batch module

we have added a simple_drush_cmd.py and a compound_drush_cmd.py file to help you make drush commands to ingest you should execute the command from the drupal root, not from within this folder (copy the command then ```cd /var/www/drupal7``` and paste it in the terminal) you are still responsible for executing your own ```drush ibi``` command on your own.

run the cleanup script to clear out old data (deletes any files in the output directory or working directory)
- ```sh cleanup.sh```

be sure to delete the zip you place in input/ before starting a new set of ingests (perhaps add to cleanup...)