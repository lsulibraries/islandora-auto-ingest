#ingest packager and nameconvention checker for louisiana digital library LDL

instructions for running the prototype:

run the cleanup script to clear out old data (deletes any files in the output directory or working directory)
```sh cleanup.sh```

unzip your files into the working directory
for example:
```unzip -d working input/yourzip.zip```


simple object procedures
this only checks the files for adherence to the naming patterns
```sh simpleprocess.sh```

compound object procedures
for compounds the files are checked for adherence to naming patterns and packaged appropriately
```sh compound_process.sh```
