import time
import board
import usb_hid

from adafruit_hid.keyboard import Keyboard

from .button import Button, ButtonConfig, RotatoryButton, RotatoryButtonConfig
from .keyparser import parse

from ..config.configloader import Config

BTN_00 = ButtonConfig(0, board.GP15, "")
BTN_01 = ButtonConfig(1, board.GP10, "")
BTN_02 = ButtonConfig(2, board.GP3, "")
BTN_03 = ButtonConfig(3, board.GP14, "")
BTN_04 = ButtonConfig(4, board.GP9, "")
BTN_05 = ButtonConfig(5, board.GP2, "")

BUTTONS = [BTN_00, BTN_01, BTN_02, BTN_03, BTN_04, BTN_05]
KEYS_PER_MINUTE = 300
KEY_DELAY = (1 / float(KEYS_PER_MINUTE / 60)) / 2


keyboard = Keyboard(usb_hid.devices)


class Keyboard:

    def __init__(self):
        self.config = Config()
        self.buttons = [Button(b) for b in BUTTONS]

    def _press_and_release(self, keys):
        for key in keys:
            keyboard.press(key)
            time.sleep(KEY_DELAY)
            keyboard.release(key)
            time.sleep(KEY_DELAY)

    def type(self, text):
        key_combo = parse(text)
        for keys in key_combo:
            self._press_and_release(keys)

    def verify(self):
        [b.verify_status() for b in self.buttons]
