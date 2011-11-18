#!/bin/bash
TODAY=$(date)
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR
./poachr.py
git add names.txt
git add nsids.txt
git commit -m "Updating $TODAY"
