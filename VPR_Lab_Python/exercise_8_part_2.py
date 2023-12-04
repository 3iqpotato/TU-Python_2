import math


def check_number_2(number):

    if number < 0:
        raise Exception('The number must be positive')

    else:
        return math.sqrt(number)