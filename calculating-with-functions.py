# CALCULATING WITH FUNCTIONS (5 KYU)
#
# This time we want to write calculations using functions and get the results.
#
# Let's have a look at some EXAMPLES:
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
#
# REQUIREMENTS:
# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations:
# plus, minus, times, dividedBy (divided_by in Ruby and Python)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Divison should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))

def zero(f = None):
    if f is not None:
        return f(0)
    return 0
def one(f = None):
    if f is not None:
        return f(1)
    return 1
def two(f = None):
    if f is not None:
        return f(2)
    return 2
def three(f = None):
    if f is not None:
        return f(3)
    return 3
def four(f = None):
    if f is not None:
        return f(4)
    return 4
def five(f = None):
    if f is not None:
        return f(5)
    return 5
def six(f = None):
    if f is not None:
        return f(6)
    return 6
def seven(f = None):
    if f is not None:
        return f(7)
    return 7
def eight(f = None):
    if f is not None:
        return f(8)
    return 8
def nine(f = None):
    if f is not None:
        return f(9)
    return 9

def plus(y):
    return lambda x: x + y
def minus(y):
    return lambda x: x - y
def times(y):
    return lambda x: x * y
def divided_by(y):
    return lambda x: x // y
