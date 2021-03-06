from machine import Pin, SPI

from max7219_driver import Max7219

spi = SPI(1, baudrate=10000000)
display = Max7219(8, 8, spi, Pin(15))


def display_character(char, x=0, y=0):
    display.text(char, x, y)
    display.show()


def light_pixel(x=0, y=0, c=1):
    display.pixel(x, y, c)
    display.show()


def light_multiple_pixels(pixels):
    for x, y in pixels.items():
        display.pixel(x, y, 1)
        display.show()


def light_v_line(x=0, y=0, w=8, c=1):
    display.vline(x, y, w, c)
    display.show()


def light_h_line(x=0, y=0, w=8, c=1):
    display.hline(x, y, w, c)
    display.show()


def clear_display():
    display.fill(0)
