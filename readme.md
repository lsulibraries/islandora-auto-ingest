#ingest packager and nameconvention checker for louisiana digital library LDL

instructions for running the prototype:
open a terminal and navigate to the path of this git repository

run the setup script to create some directories to work in:

```sh setup.sh```



copy your zipped files to the input folder
for example:
```cp ~/Downloads/yourfiles.zip input/```

simple object procedures
this only checks the files for adherence to the naming patterns
```sh simpleprocess.sh```

compound object procedures
for compounds the files are checked for adherence to naming patterns and packaged appropriately
```sh compound_process.sh```

run the cleanup script to clear out old data (deletes any files in the output directory or working directory)
```sh cleanup.sh```