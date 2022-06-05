from time import sleep

from display import light_pixel, light_multiple_pixels, clear_display, light_v_line, light_h_line


def night_rider(sleep_time=0.1):
    x_axis_asc(0, 7, 4, sleep_time)
    x_axis_desc(7, 0, 4, sleep_time)


def chase_edge(sleep_time=0.1):
    x_axis_asc(0, 7, 0, sleep_time)
    y_axis_asc(0, 7, 7, sleep_time)
    x_axis_desc(7, 0, 7, sleep_time)
    y_axis_desc(7, 0, 0, sleep_time)


def spiral(sleep_time=0.1):
    x_axis_asc(0, 7, 0, sleep_time)
    y_axis_asc(0, 7, 7, sleep_time)
    x_axis_desc(7, 0, 7, sleep_time)
    y_axis_desc(7, 0, 0, sleep_time)

    x_axis_asc(1, 6, 1, sleep_time)
    y_axis_asc(1, 6, 6, sleep_time)
    x_axis_desc(6, 1, 6, sleep_time)
    y_axis_desc(6, 1, 1, sleep_time)

    x_axis_asc(2, 5, 2, sleep_time)
    y_axis_asc(2, 5, 5, sleep_time)
    x_axis_desc(5, 2, 5, sleep_time)
    y_axis_desc(5, 2, 2, sleep_time)

    x_axis_asc(3, 4, 3, sleep_time)
    y_axis_asc(3, 4, 4, sleep_time)
    x_axis_desc(4, 3, 4, sleep_time)
    y_axis_desc(4, 3, 3, sleep_time)


def windmill(sleep_time=0.1):
    diagonal_l_r = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}
    light_multiple_pixels(diagonal_l_r)
    sleep(sleep_time)
    clear_display()

    light_h_line(0, 4, 8, 1)
    sleep(sleep_time)
    clear_display()

    diagonal_r_1 = {7: 0, 6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 7}
    light_multiple_pixels(diagonal_r_1)
    sleep(sleep_time)
    clear_display()

    light_v_line(4, 0, 8, 1)
    sleep(sleep_time)
    clear_display()


def l_r_fill(sleep_time=0.1):
    y = 0
    while y < 8:
        light_h_line(0, y, 8, 1)
        sleep(sleep_time)
        y += 1
    clear_display()


def l_r_sweep(sleep_time=0.1):
    y = 0
    while y < 8:
        light_h_line(0, y, 8, 1)
        sleep(sleep_time)
        y += 1
        clear_display()


def r_l_fill(sleep_time=0.1):
    y = 7
    while y != -1:
        light_h_line(0, y, 8, 1)
        sleep(sleep_time)
        y -= 1
    clear_display()


def r_l_sweep(sleep_time=0.1):
    y = 7
    while y != -1:
        light_h_line(0, y, 8, 1)
        sleep(sleep_time)
        y -= 1
        clear_display()


def t_b_fill(sleep_time=0.1):
    y = 0
    while y < 8:
        light_v_line(y, 0, 8, 1)
        sleep(sleep_time)
        y += 1
    clear_display()


def b_t_fill(sleep_time=0.1):
    y = 7
    while y != -1:
        light_v_line(y, 0, 8, 1)
        sleep(sleep_time)
        y -= 1
    clear_display()


def x_axis_asc(start, stop, y, sleep_time):
    while start < stop:
        light_pixel(start, y)
        sleep(sleep_time)
        start += 1
        clear_display()


def x_axis_desc(start, stop, y, sleep_time):
    while start > stop:
        light_pixel(start, y)
        sleep(sleep_time)
        start -= 1
        clear_display()


def y_axis_asc(start, stop, x, sleep_time):
    while start < stop:
        light_pixel(x, start)
        sleep(sleep_time)
        start += 1
        clear_display()


def y_axis_desc(start, stop, x, sleep_time):
    while start > stop:
        light_pixel(x, start)
        sleep(sleep_time)
        start -= 1
        clear_display()
