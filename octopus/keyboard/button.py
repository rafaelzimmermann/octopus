import digitalio
import collections

ButtonConfig = collections.namedtuple('ButtonConfig', ['index', 'pin', 'action'])


class Button:

    def __init__(self, button_config: ButtonConfig):
        self._gpio = digitalio.DigitalInOut(button_config.pin)
        self._gpio.direction = digitalio.Direction.INPUT
        self._gpio.pull = digitalio.Pull.DOWN
        self.click_callbacks = []

    def on_click(self, callback):
        self.click_callbacks.append(callback)

    def verify_status(self):
        if self._gpio.value:
            for callback in self.click_callbacks:
                callback()
