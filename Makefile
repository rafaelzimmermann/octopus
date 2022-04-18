

clean:
	./scripts/clean.sh

deploy: clean
	./scripts/deploy-dir.sh .

deploy-uf2:
	cp rp2-pico-20220117-v1.18.uf2 /Volumes/RPI-RP2

deploy-cp-uf2:
	cp adafruit-circuitpython-raspberry_pi_pico-en_US-7.2.5.uf2 /Volumes/RPI-RP2