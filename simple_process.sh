#!/bin/bash
unzip -d working input/*
python3 naming_pattern_checks.py
mv working/* output/
