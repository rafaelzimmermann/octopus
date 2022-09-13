import digitalio
import collections

ButtonConfig = collections.namedtuple('ButtonConfig', ['index', 'pin', 'action'])


def execute_callbacks(callbacks):
    [c() for c in callbacks]


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


RotatoryButtonConfig = collections.namedtuple('RotatoryButtonConfig', ['index', 'sw_pin', 'dt_pin', 'clk_pin'])


class RotatoryButton:

    def __init__(self, config: RotatoryButtonConfig):
        self.config = config

        self._sw_gpio = digitalio.DigitalInOut(config.sw_pin)
        self._sw_gpio.direction = digitalio.Direction.INPUT
        self._sw_gpio.pull = digitalio.Pull.UP

        self._dt_gpio = digitalio.DigitalInOut(config.dt_pin)
        self._dt_gpio.direction = digitalio.Direction.INPUT
        self._dt_gpio.pull = digitalio.Pull.UP

        self._clk_gpio = digitalio.DigitalInOut(config.clk_pin)
        self._clk_gpio.direction = digitalio.Direction.INPUT
        self._clk_gpio.pull = digitalio.Pull.UP

        self.click_callbacks = []
        self.rotation_right_callbacks = []
        self.rotation_left_callbacks = []

    def on_click(self, callback):
        self.click_callbacks.append(callback)

    def on_left(self, callback):
        self.rotation_left_callbacks.append(callback)

    def on_right(self, callback):
        self.rotation_right_callbacks.append(callback)

    def verify_status(self):
        if not self._sw_gpio.value:
            execute_callbacks(self.click_callbacks)

        if self._dt_gpio.value != self._clk_gpio.value and self._dt_gpio.value:
            execute_callbacks(self.rotation_left_callbacks)
        if self._dt_gpio.value != self._clk_gpio.value and self._clk_gpio.value:
            execute_callbacks(self.rotation_right_callbacks)

