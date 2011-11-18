#!/bin/bash
TODAY=$(date)
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR
./poachr.py
git diff --exit-code
if [ "$?" -ne "0" ]; then
  git add names.txt
  git add nsids.txt
  git commit -m "Updating $TODAY"
  git push origin master
fi
