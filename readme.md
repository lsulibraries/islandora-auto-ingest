readme.md

#auto-ingest for louisiana digital library LDL

#instructions

#configure box api.

#install by copying run-auto-ingest.sh to a path to be run by cron every minute for testing purposes

#crontab -e 

#write 

0 * * * * * run-auto-ingest.sh


#run-auto-ingest.sh script to trigger a round of ingest processes based on a cyclic pattern

#server_prepocessing.py 
#naming_pattern_checks.py
#packaging.py
#drush_command_population.py
#logging.py
#cleanup.py


#todo populate sample files, simple and compound,
#several possible ways of unzipping the files/ scrabmling/changing the names for tests etc must be created

#input folder for files to be unzipped into
#output is a destination for packaged files ready for ingest preprocessing
#log writes history of failures and successful uploads, keeps one handoff file in final state after last process run

