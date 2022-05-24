import board
import digitalio
import time
import usb_hid

from adafruit_hid.keyboard import Keyboard
from display import Display
from keyparser import parse
from button import Button

BTN_00 = board.GP16
BTN_01 = board.GP17
BTN_02 = board.GP18
BTN_03 = board.GP19
BTN_04 = board.GP20
BTN_05 = board.GP9
BTN_06 = board.GP8
BTN_07 = board.GP7
BTN_08 = board.GP6
BTN_09 = board.GP4
BTN_10 = board.GP22
BTN_11 = board.GP26
BTN_12 = board.GP27
BUTTONS = [BTN_00, BTN_01, BTN_02, BTN_03, BTN_04, BTN_05, BTN_06, BTN_07, BTN_08, BTN_09, BTN_10, BTN_11, BTN_12]
KEYS_PER_MINUTE = 300
KEY_DELAY = (1 / float(KEYS_PER_MINUTE / 60)) / 2
TEST_MODE = False

keyboard = Keyboard(usb_hid.devices)


class Octopus:
    def __init__(self):
        self.mute = None
        self.setup()

    def setup(self):
        self.buttons = [Button(b) for b in BUTTONS]
        self.buttons[0].on_click(lambda: self.type("test"))
        self.led = digitalio.DigitalInOut(board.LED)
        self.led.direction = digitalio.Direction.OUTPUT
        self.display = Display()

    def init(self):
        self.display.splash()
        for i in range(0, 5):
            self.blink_led()

    def press_and_release(self, key):
        keyboard.press(key)
        self.led.value = True
        time.sleep(KEY_DELAY)
        self.led.value = False
        keyboard.release(key)
        time.sleep(KEY_DELAY)

    def blink_led(self):
        self.led.value = True
        time.sleep(KEY_DELAY)
        self.led.value = False
        time.sleep(KEY_DELAY)

    def type(self, text):
        keys = parse(text)
        typed = ""
        self.display.clear()
        for key in keys:
            if TEST_MODE:
                self.blink_led()
            else:
                typed += key.char
                self.display.print_message(typed)
                self.press_and_release(key.code)
        self.display.splash()

    def run(self):
        self.init()
        while True:
            [b.verify_status() for b in self.buttons]
            time.sleep(0.1)


if __name__ == '__main__':
    octopus = Octopus()
    octopus.run()
