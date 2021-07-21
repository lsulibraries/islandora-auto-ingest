#ingest packager and nameconvention checker for louisiana digital library LDL

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


run the cleanup script to clear out old data (deletes any files in the output directory or working directory)
- ```sh cleanup.sh```

