#!/bin/bash


set -ex

dir="/media/${USER}/CIRCUITPY/"
tmpdir=$(mktemp -d)
if [[ $OSTYPE == 'darwin'* ]]; then
  dir="/Volumes/CIRCUITPY/lib/"
fi

unzip resources/adafruit-circuitpython-hid-7.x-mpy-5.2.2.zip -d $tmpdir/hid-lib
cp -r $tmpdir/hid-lib/adafruit-circuitpython-hid-7.x-mpy-5.2.2/lib/adafruit_hid $dir
