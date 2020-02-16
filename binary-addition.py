# BINARY ADDITION (7 KYU)
#
# Implement a function that adds two numbers together and returns their sum in binary.
# The conversion can be done before, or after the addition.
#
# The binary number returned should be a string.

def add_binary(a,b):
    if a == 0 and b == 0:
        return ''
    c = a + b
    return add_binary(c // 2, 0) + str(c % 2)
