# MULTIPLES OF 3 OR 5 (6 KYU)
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
#
# NOTE: If the number is a multiple of both 3 and 5, only count it once.

def solution(number):
    counter = 0
    three_val = 3
    while number > three_val:
        counter += three_val
        three_val += 3
    five_val = 5
    while number > five_val:
        counter += five_val
        five_val += 5
    fifteen_val = 15
    while number > fifteen_val:
        counter -= fifteen_val
        fifteen_val += 15
    return counter
