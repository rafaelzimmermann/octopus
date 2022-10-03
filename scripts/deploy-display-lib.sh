#!/bin/bash


set -ex

dir="/media/${USER}/CIRCUITPY"
tmpdir=$(mktemp -d)
if [[ $OSTYPE == 'darwin'* ]]; then
  dir="/Volumes/CIRCUITPY"
fi

unzip resources/adafruit-circuitpython-display-text-py-2.22.3.zip -d $tmpdir/display-text
cp -r $tmpdir/display-text/adafruit-circuitpython-display-text-py-2.22.3/lib/adafruit_display_text $dir/lib/

unzip resources/adafruit-circuitpython-displayio-ssd1306-py-1.5.3.zip -d $tmpdir/display-text
cp -r $tmpdir/display-text/adafruit-circuitpython-displayio-ssd1306-py-1.5.3/lib/adafruit_displayio_ssd1306.py $dir/lib/
