import time
import board
import usb_hid

from adafruit_hid.keyboard import Keyboard

from .button import Button, ButtonConfig
from .keyparser import parse

from ..config.configloader import Config

BTN_00 = ButtonConfig(0, board.GP16, "")
BTN_01 = ButtonConfig(1, board.GP17, "")
BTN_02 = ButtonConfig(2, board.GP18, "")
BTN_03 = ButtonConfig(3, board.GP19, "")
BTN_04 = ButtonConfig(4, board.GP20, "")
BTN_05 = ButtonConfig(5, board.GP9, "")
BTN_06 = ButtonConfig(6, board.GP8, "")
BTN_07 = ButtonConfig(7, board.GP7, "")
BTN_08 = ButtonConfig(8, board.GP6, "")
BTN_09 = ButtonConfig(9, board.GP4, "")
BTN_10 = ButtonConfig(10, board.GP22, "")
BTN_11 = ButtonConfig(11, board.GP26, "")
BTN_12 = ButtonConfig(12, board.GP27, "")
BUTTONS = [BTN_00, BTN_01, BTN_02, BTN_03, BTN_04, BTN_05, BTN_06, BTN_07, BTN_08, BTN_09, BTN_10, BTN_11, BTN_12]
KEYS_PER_MINUTE = 300
KEY_DELAY = (1 / float(KEYS_PER_MINUTE / 60)) / 2


keyboard = Keyboard(usb_hid.devices)


class Keyboard:

    def __init__(self):
        self.config = Config()
        self.buttons = [Button(b) for b in BUTTONS]

    def _press_and_release(self, keys):
        print(keys)
        for key in keys:
            keyboard.press(key)
            time.sleep(KEY_DELAY)
            keyboard.release(key)
            time.sleep(KEY_DELAY)

    def type(self, text):
        key_combo = parse(text)
        print(key_combo)
        for keys in key_combo:
            self._press_and_release(keys)

    def verify(self):
        [b.verify_status() for b in self.buttons]