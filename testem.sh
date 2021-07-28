#!/bin/bash
for entry in "sample_data"/*
do
  unzip -d working "$entry" 
  python3 naming_pattern_checks.py
  rm working/*
done
