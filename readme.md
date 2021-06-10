#auto-ingest for louisiana digital library LDL

instructions for running the prototype:

first run the setup script to create needed directories input and output and working

```sh setup.sh```


add files from the suggested sample_data folder to the input folder (where they remain zipped)

ie 

```cp sample_data/<zipfile_name>.zip input```

to run both the naming_pattern_checks and the packaging script senquentially execute:

```sh go.sh```


to clean up files in the working and output directory to both steps again execute:
```sh cleanup.sh```
Then you are ready to run
```sh go.sh``` again.


If you want new sample data, just remove the current data in input
```rm input/*```









These represent instructions from an earlier planning stage.
#instructions: 

#this application is designed to be deployed on the LDL ingest server which resides on AWS.

#Original plan to deploy on hold. developing two part process for now, to simplify.



#testing.py should test each process and function with sample data

#server_prepocessing.py prototype ready
#naming_pattern_checks.py prototype in progress
#packaging.py
#drush_command_population.py
#logging.py
#cleanup.py

#input/
#output/


#todo now:

#namming_pattern_checks.py
#packaging.py



#todo later:

#create several ways of unzipping the files/ scrabmling/changing the names for tests etc must be created
#log writes history of failures and successful uploads, keeps one handoff file in final state after last process run

#install by copying run-auto-ingest.sh to a path to be run by cron every minute for testing purposes

#run-auto-ingest.sh script to trigger a round of ingest processes based on a cyclic pattern
```crontab -e```
#add this line
```0 * * * * * run-auto-ingest.sh```
#configure box api. 