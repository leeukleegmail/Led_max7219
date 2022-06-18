from machine import RTC

import patterns

rtc = RTC()
rtc.datetime((2017, 8, 23, 1, 12, 48, 0, 0))  # set a specific date and time


def run_pattern(sequence):
    if sequence == "0":
        patterns.windmill(0.1)
    if sequence == "1":
        patterns.night_rider(0.05)
    if sequence == "2":
        patterns.spiral(0)
    if sequence == "3":
        patterns.chase_edge(0.05)
    if sequence == "4":
        patterns.l_r_fill(0.1)
    if sequence == "5":
        patterns.r_l_fill(0.1)
    if sequence == "6":
        patterns.l_r_sweep(0.1)
    if sequence == "7":
        patterns.r_l_sweep(0.1)
    if sequence == "8":
        patterns.t_b_fill(0.1)
    if sequence == "9":
        patterns.b_t_fill(0.1)


def randomish_number():
    datetime = rtc.datetime()[-1]
    return str(datetime)[-1]


while True:
    sequence = randomish_number()
    run_pattern(sequence)
