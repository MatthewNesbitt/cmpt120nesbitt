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

