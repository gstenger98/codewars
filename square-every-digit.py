# SQUARE EVERY DIGIT (7 KYU)
#
# Welcome. In this kata, you are asked to square every digit of a number.
#
# For EXAMPLE, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
#
# NOTE: The function accepts an integer and returns an integer

def square_digits(num):
    if len(str(num)) > 1:
        leftdigitsquared = square_digits(num // (10 ** (int(len(str(num))) - 1)))
        remainingdigits = num % (10 ** (int(len(str(num))) - 1))
        return int(str(leftdigitsquared) + str(square_digits(remainingdigits)))
    else:
        return num ** 2

print(square_digits(7897123))
