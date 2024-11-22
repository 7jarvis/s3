import random

START_VALUE_FOR_SLIDER = 1
STOP_VALUE_FOR_SLIDER = 9


def get_random_num():
    n = random.randrange(START_VALUE_FOR_SLIDER, STOP_VALUE_FOR_SLIDER)
    return n
