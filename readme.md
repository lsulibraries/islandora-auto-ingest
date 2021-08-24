## ingest packager and nameconvention checker for louisiana digital library LDL

instructions for use on the server

scp your zipfile to the ingest server /tmp directory

- ```scp -i ~/path_to_key <zipped_files>.zip <user@dgi-ingest-ip-address>:/tmp```

log into the ldl ingest server via ssh (from command prompt or git bash):

- ```ssh -i ~/path_to_key <user@dgi-ingest-ip-address>```

navigate to /etc/islandora-auto-ingest:

- ```cd /etc/islandora-auto-ingest```

move your files to the input folder:

- ```sudo mv /tmp/<zipped_files>.zip input/```



The next command will check your files for adherence to the naming convention, and report any errors.
If it finishes the check without error it will continue to packaging, and then drush command population.

Choose one:

1.  simple object ingest procedure:

- ```sudo sh simpleprocess.sh```

2.  compound object ingest procedure:

- ```sudo sh compound_process.sh```



Copy the outputted drush command (right click with mouse from terminal)


change into the drupal root:

- ```cd /var/www/drupal7```

paste the command into the terminal and press enter:

The command will pre-process, and should finishe with an ingest set number:

execute the ingest command:

- ```drush -u 1 ibi --ingest_set=<ingest_set_number>```

This script will delete all the files in the output directory and working directory. run it after you are finished:

- ```sudo sh cleanup.sh```

delete the copy from input only when you are sure everything is correct. If anything went wrong or files need to be renamed this acts as a backup for the ingest until you delete it. (don't run this procedure with multiple zip files in the input directory)

- ```sudo rm input/*```




