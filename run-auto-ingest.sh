#run-auto-ingest.sh
#!/bin/bash
python3 server preprocessing.py
python3 naming_pattern_checks.py
python3 packaging.py
python3 drush_command_population.py
python3 logging.py
python3 cleanup.py



