#!/bin/bash
for entry in "sample_data"/*
do
  echo "$entry"
  unzip -q -d working "$entry"
  python3 naming_pattern_checks.py
  rm working/*
done
