import digitalio


class Button:

    def __init__(self, pin):
        self.mute = digitalio.DigitalInOut(pin)
        self.mute.direction = digitalio.Direction.INPUT
        self.mute.pull = digitalio.Pull.DOWN
        self.click_callbacks = []

    def on_click(self, callback):
        self.click_callbacks.append(callback)

    def verify_status(self):
        if self.mute.value:
            for callback in self.click_callbacks:
                callback()
