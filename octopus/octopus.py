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
        self.keyboard.buttons[0].on_click(lambda: self.keyboard.type("test"))

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
