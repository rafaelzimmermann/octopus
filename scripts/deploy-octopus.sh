#!/bin/bash

set -ex

dir="/media/${USER}/CIRCUITPY"
if [[ $OSTYPE == 'darwin'* ]]; then
  dir="/Volumes/CIRCUITPY"
fi

if [[ -f "$dir/code.py" ]]; then
  rm -irf $dir/*.py
fi

if [[ -d "$dir/octopus" ]]; then 
  rm -irf $dir/octopus
fi

cp -r *.py *.json octopus $dir/