# Adapting the example in https://learn.adafruit.com/adafruit-oled-featherwing/python-usage
# to use with Raspberry Pi Pico and CircuitPython

import board
import busio
import displayio
import terminalio
import time

from adafruit_displayio_ssd1306 import SSD1306
from adafruit_display_text import label

WHITE = 0xFFFFFF
BLACK = 0x000000
WIDTH = 128
HEIGHT = 64


class DisplayBase:

    def __init__(self):
        displayio.release_displays()
        i2c = busio.I2C(scl=board.GP11, sda=board.GP10)  # This RPi Pico way to call I2C
        display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)  # The address of my Board
        self.display = SSD1306(display_bus, width=WIDTH, height=HEIGHT)
        self._canvas = None

    @property
    def canvas(self):
        if self._canvas is None:
            self._canvas = displayio.Group()
            self.display.show(self._canvas)
        return self._canvas

    def done(self):
        self._canvas = None

    def solid_rectangle(self, width, height, x, y, color):
        color_bitmap = displayio.Bitmap(width, height, 1)
        color_palette = displayio.Palette(1)
        color_palette[0] = color
        self.canvas.append(
            displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=x, y=y)
        )

    def rectangle(self, width, height, thickness, x, y, color):
        self.solid_rectangle(width, height, x, y, color)
        inner_color = BLACK if color == WHITE else WHITE
        inner_width = width - thickness
        inner_height = height - thickness
        inner_x = x + thickness // 2
        inner_y = y + thickness // 2
        self.solid_rectangle(inner_width, inner_height, inner_x, inner_y, inner_color)

    def simple_message(self, text, color=WHITE, x=0, y=int(HEIGHT/2)):
        text_area = label.Label(terminalio.FONT, text=text, color=color, x=x, y=y)
        self.canvas.append(text_area)

    def clear(self):
        self.done()
        self.solid_rectangle(WIDTH, HEIGHT, 0, 0, BLACK)

    def rectangle_animation(self):
        step = 10
        thickness = 10
        for w in range(WIDTH, 20, -step):
            h = w * HEIGHT // WIDTH
            x = WIDTH - w
            x = x if x == 0 else x // 2
            y = HEIGHT - h
            y = y if y == 0 else y // 2
            self.rectangle(w, h, thickness, x, y, WHITE)
            time.sleep(0.1)
            self.clear()
