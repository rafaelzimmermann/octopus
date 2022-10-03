#!/bin/bash


set -ex

if [[ $OSTYPE == 'darwin'* ]]; then
  cp resources/adafruit-circuitpython-raspberry_pi_pico-en_US-7.2.5.uf2 /Volumes/RPI-RP2
fi

if [[ $OSTYPE == 'linux'* ]]; then
  device=$(sudo blkid -o list | grep RPI-RP2 | grep -o "/dev/[^ ]*")
  sudo mkdir -p /mnt/pico
  sudo mount $device /mnt/pico
  cp resources/adafruit-circuitpython-raspberry_pi_pico-en_US-7.2.5.uf2 /mnt/pico
  sudo sync
fi