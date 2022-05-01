

deploy:
	rm /Volumes/CIRCUITPY/*.py; cp *.py /Volumes/CIRCUITPY/

deploy-uf2:
	cp resources/rp2-pico-20220117-v1.18.uf2 /Volumes/RPI-RP2

deploy-cp-uf2:
	cp resources/adafruit-circuitpython-raspberry_pi_pico-en_US-7.2.5.uf2 /Volumes/RPI-RP2

deploy-hid-lib:
	unzip resources/adafruit-circuitpython-hid-7.x-mpy-5.2.2.zip -d /tmp/hid-lib; cp -r /tmp/hid-lib/adafruit-circuitpython-hid-7.x-mpy-5.2.2/lib/adafruit_hid /Volumes/CIRCUITPY/lib/
