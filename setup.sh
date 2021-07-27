#!/bin/bash
mkdir input
mkdir working
mkdir output
sudo apt install php-xml
sudo apt install php7.4-cli
sudo apt install git
git clone https://github.com/lsulibraries/islandora_compound_batch
git clone https://github.com/lsulibraries/islandora-auto-ingest
