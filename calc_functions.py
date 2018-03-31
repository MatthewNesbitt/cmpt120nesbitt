# Math functions for calulator

from math import *

def addition(num1, num2):
    result = num1 + num2
    return float (result)

def subtraction(num1, num2):
    result = num1 - num2
    return float (result)

def multiplication(num1, num2):
    result = num1 * num2
    return float (result)

def division(num1, num2):
    result = num1 / num2
    return float (result)

def change_sign(num1):
    result = (num1 * -1)
    return float (result)

def square(num1):
    result = num1 * num1
    return float (result)

def square_root (num1):
    result = sqrt(num1)
    return float (result)

def percent (num1):
    result = num1 / 100
    return float (result)

def over_x(num1):
    x = num1
    result = 1 / x
    return float (result)

def sine (num1):
    result = sin(num1)
    return float (result)

def cosine (num1):
    result = cos(num1)
    return float (result)

def tangent (num1):
    result = tan(num1)
    return float(result)

def power_of_ten(num1):
    result = 10 ** num1
    return float(result)

def log_button(num1):
    result = log10(num1)
    return float(result)

def natural_log(num1):
    result = log(num1)
    return float(result)

def arc_sin(num1):
    result = asin(num1)
    return float(result)

def arc_cos(num1):
    result = acos(num1)
    return float(result)

def arc_tan(num1):
    result = atan(num1)
    return float(result)

def x_to_the_y(num1, num2):
    result = num1 ** num2
    return float(result)

