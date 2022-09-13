import board
import digitalio
import time

from .keyboard.keyboard import Keyboard

TEST_MODE = False
LED_DELAY = 0.1


class Octopus:
    def __init__(self):
        self.led = digitalio.DigitalInOut(board.LED)
        self.led.direction = digitalio.Direction.OUTPUT
        self.keyboard = Keyboard()
        self.setup()

    def setup(self):
        self.keyboard.buttons[0].on_click(lambda: self.keyboard.type("0"))
        self.keyboard.buttons[1].on_click(lambda: self.keyboard.type("1"))
        self.keyboard.buttons[2].on_click(lambda: self.keyboard.type("2"))
        self.keyboard.buttons[3].on_click(lambda: self.keyboard.type("3"))
        self.keyboard.buttons[4].on_click(lambda: self.keyboard.type("4"))
        self.keyboard.buttons[5].on_click(lambda: self.keyboard.type("5"))



    def start_up(self):
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
