from time import sleep

from display import light_pixel

sleep_time = 0.25

while True:
    x = 0
    while x < 8:
        light_pixel(x)
        x += 1
        sleep(sleep_time)
    x -= 1
    while x > 1:
        x -= 1
        light_pixel(x)
        sleep(sleep_time)
