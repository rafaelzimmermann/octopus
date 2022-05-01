import board
import digitalio
import time
import usb_hid

from adafruit_hid.keyboard import Keyboard
from keyparser import parse


keyboard = Keyboard(usb_hid.devices)

key_map = {

}


class Octopus:

    def __init__(self):
        self.mute = None
        self.setup()

    def setup(self):
        self.mute = digitalio.DigitalInOut(board.GP26)
        self.mute.direction = digitalio.Direction.INPUT
        self.mute.pull = digitalio.Pull.DOWN
        self.led = digitalio.DigitalInOut(board.LED)
        self.led.direction = digitalio.Direction.OUTPUT


    def press_and_release(self, key):
        keyboard.press(key)
        self.led.value = True
        time.sleep(0.01)
        self.led.value = False
        keyboard.release(key)

    def run(self):
        while True:
            if self.mute.value:
                keys = parse("Hello World")
                for key in keys:
                    self.press_and_release(key)

            time.sleep(0.1)


if __name__ == '__main__':
    octopus = Octopus()
    octopus.run()
