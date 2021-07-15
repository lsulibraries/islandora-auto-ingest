#!/bin/bash
unzip -d  working input/*
python3 naming_pattern_checks.py
python3 packaging.py
