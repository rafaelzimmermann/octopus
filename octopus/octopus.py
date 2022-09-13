import board
import digitalio
import time

from .display import Display
from .keyboard.keyboard import Keyboard

TEST_MODE = False
LED_DELAY = 0.1


class Octopus:
    def __init__(self):
        self.led = digitalio.DigitalInOut(board.LED)
        self.led.direction = digitalio.Direction.OUTPUT
        self.display = Display()
        self.keyboard = Keyboard()
        self.setup()

    def setup(self):
        self.keyboard.buttons[0].on_click(lambda: self.keyboard.type("0"))
        self.keyboard.buttons[1].on_click(lambda: self.keyboard.type("1"))
        self.keyboard.buttons[2].on_click(lambda: self.keyboard.type("2"))

        self.keyboard.rotatory_button0.on_click(lambda: self.keyboard.type("Rotatory button 0"))
        self.keyboard.rotatory_button0.on_left(lambda: self.keyboard.type("L"))
        self.keyboard.rotatory_button0.on_right(lambda: self.keyboard.type("R"))

        self.keyboard.rotatory_button1.on_click(lambda: self.keyboard.type("Rotatory button 1"))
        self.keyboard.rotatory_button1.on_left(lambda: self.keyboard.type("L1"))
        self.keyboard.rotatory_button1.on_right(lambda: self.keyboard.type("R1"))

    def start_up(self):
        self.display.splash()
        for i in range(0, 5):
            self.blink_led()

    def blink_led(self):
        self.led.value = True
        time.sleep(LED_DELAY)
        self.led.value = False
        time.sleep(LED_DELAY)

    def run(self):
        self.start_up()
        while True:
            self.keyboard.verify()
            time.sleep(0.1)
