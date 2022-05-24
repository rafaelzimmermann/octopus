import time

from displaybase import DisplayBase, WIDTH, HEIGHT, WHITE


class Display:
    def __init__(self, display_base=DisplayBase()):
        self._base = display_base

    def click_button_effect(self):
        self._base.solid_rectangle(WIDTH, HEIGHT, 0, 0, WHITE)
        time.sleep(0.2)
        self._base.clear()

    def splash(self):
        self._base.rectangle(WIDTH, HEIGHT, 10, 0, 0, WHITE)
        self._base.simple_message("Octopus 1.0", WHITE, 28, 15)

    def print_message(self, message, x=0, y=int(HEIGHT / 2)):
        self._base.simple_message(message, x=x, y=y)

    def clear(self):
        self._base.clear()

