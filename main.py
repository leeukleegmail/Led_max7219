from machine import RTC

import patterns

rtc = RTC()
rtc.datetime((2017, 8, 23, 1, 12, 48, 0, 0))  # set a specific date and time


def run_pattern(pattern):
    if pattern == "0":
        patterns.windmill(0.1)
    if pattern == "1":
        patterns.night_rider(0.05)
    if pattern == "2":
        patterns.spiral(0)
    if pattern == "3":
        patterns.chase_edge(0.05)
    if pattern == "4":
        patterns.l_r_fill(0.1)
    if pattern == "5":
        patterns.r_l_fill(0.1)
    if pattern == "6":
        patterns.l_r_sweep(0.1)
    if pattern == "7":
        patterns.r_l_sweep(0.1)
    if pattern == "8":
        patterns.t_b_fill(0.1)
    if pattern == "9":
        patterns.b_t_fill(0.1)


def randomish_number():
    datetime = rtc.datetime()[-1]
    return str(datetime)[-1]


while True:
    run_pattern(randomish_number())
