

deploy:
	rm -rf /Volumes/CIRCUITPY/*.py rm -rf /Volumes/CIRCUITPY/*.json /Volumes/CIRCUITPY/octopus; cp -r *.py *.json octopus /Volumes/CIRCUITPY/

deploy-uf2:
	cp resources/rp2-pico-20220117-v1.18.uf2 /Volumes/RPI-RP2

deploy-cp-uf2:
	cp resources/adafruit-circuitpython-raspberry_pi_pico-en_US-7.2.5.uf2 /Volumes/RPI-RP2

deploy-hid-lib:
	unzip resources/adafruit-circuitpython-hid-7.x-mpy-5.2.2.zip -d /tmp/hid-lib; cp -r /tmp/hid-lib/adafruit-circuitpython-hid-7.x-mpy-5.2.2/lib/adafruit_hid /Volumes/CIRCUITPY/lib/

deploy-adafruit-display-lib:
	unzip resources/adafruit-circuitpython-display-text-py-2.22.3.zip -d /tmp/display-text; cp -r /tmp/display-text/adafruit-circuitpython-display-text-py-2.22.3/lib/adafruit_display_text /Volumes/CIRCUITPY/lib/
	unzip resources/adafruit-circuitpython-displayio-ssd1306-py-1.5.3.zip -d /tmp/display-text; cp -r /tmp/display-text/adafruit-circuitpython-displayio-ssd1306-py-1.5.3/lib/adafruit_displayio_ssd1306.py /Volumes/CIRCUITPY/lib/
