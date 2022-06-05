from machine import RTC

from patterns import windmill, night_rider, r_l_fill, l_r_fill, chase_edge, spiral, r_l_sweep, l_r_sweep, t_b_fill, \
    b_t_fill

rtc = RTC()
rtc.datetime((2017, 8, 23, 1, 12, 48, 0, 0))  # set a specific date and time
datetime = rtc.datetime()[-1]  # get date and time

while True:
    datetime = rtc.datetime()[-1]
    sequence = str(datetime)[-1]
    if sequence == "0":
        windmill(0.1)
    if sequence == "1":
        night_rider(0.05)
    if sequence == "2":
        spiral(0)
    if sequence == "3":
        chase_edge(0.05)
    if sequence == "4":
        l_r_fill(0.1)
    if sequence == "5":
        r_l_fill(0.1)
    if sequence == "6":
        l_r_sweep(0.1)
    if sequence == "7":
        r_l_sweep(0.1)
    if sequence == "8":
        t_b_fill(0.1)
    if sequence == "9":
        b_t_fill(0.1)
