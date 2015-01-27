import random
from math import sin, cos, tan, pi, sqrt, atan
from expression_builder import generate_expression

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""

    expression = generate_expression()
    return expression


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return eval(expr)

def avg(x, y):
    return (x + y) / 2

def average_3(x, y, z):
    return (x + y + z) / 3

def square(x):
    if x > 0:
        return x**2
    else:
        return x**2 * -1

def cube(x):
    return x**3

def root(x):
    if x < 0:
        x *= -1
        sqrt(x)
        return x * -1
    else:
        return sqrt(x)
