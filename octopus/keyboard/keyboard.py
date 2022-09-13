import time
import board
import usb_hid

from adafruit_hid.keyboard import Keyboard

from .button import Button, ButtonConfig, RotatoryButton, RotatoryButtonConfig
from .keyparser import parse

from ..config.configloader import Config

BTN_00 = ButtonConfig(0, board.GP16, "")
BTN_01 = ButtonConfig(9, board.GP21, "")
BTN_02 = ButtonConfig(10, board.GP22, "")

ROTATORY_BTN_00 = RotatoryButtonConfig(0, board.GP20, board.GP19, board.GP18)
ROTATORY_BTN_01 = RotatoryButtonConfig(1, board.GP12, board.GP11, board.GP13)

BUTTONS = [BTN_00, BTN_01, BTN_02]
KEYS_PER_MINUTE = 1000
KEY_DELAY = (1 / float(KEYS_PER_MINUTE / 60)) / 2


keyboard = Keyboard(usb_hid.devices)


class Keyboard:

    def __init__(self):
        self.config = Config()
        self.buttons = [Button(b) for b in BUTTONS]
        self.rotatory_button0 = RotatoryButton(ROTATORY_BTN_00)
        self.rotatory_button1 = RotatoryButton(ROTATORY_BTN_01)

    def _press_and_release(self, keys):
        print(keys)
        for key in keys:
            keyboard.press(key)
            time.sleep(KEY_DELAY)
            keyboard.release(key)
            time.sleep(KEY_DELAY)

    def type(self, text):
        key_combo = parse(text)
        print(text)
        # for keys in key_combo:
        #     self._press_and_release(keys)

    def verify(self):
        [b.verify_status() for b in self.buttons]
        self.rotatory_button0.verify_status()
        self.rotatory_button1.verify_status()
