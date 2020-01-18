# PRODUCT OF CONSECUTIVE FIBONACCI NUMBERS (5 KYU)
#
# The Fibonacci numbers are the numbers in the following integer sequence (Fn):
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
# such as
# F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.
#
# Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying
# F(n) * F(n+1) = prod.
#
# Your function productFib takes an integer (prod) and returns an array:
# [F(n), F(n+1), true]
#
# If you don't find two consecutive F(m) verifying F(m) * F(m+1) = prodyou will return
# [F(m), F(m+1), false]
# F(m) being the smallest one such as F(m) * F(m+1) > prod.
#
# EXAMPLES:
# productFib(714) # should return [21, 34, true],
#                 # since F(8) = 21, F(9) = 34 and 714 = 21 * 34
#
# productFib(800) # should return [34, 55, false],
#                 # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55

def productFib(prod):
    f_i = 0
    f_i_plus_one = 1
    while 1 != 2:
        if f_i * f_i_plus_one == prod:
            return [f_i, f_i_plus_one, True]
        if f_i * f_i_plus_one > prod:
            return [f_i, f_i_plus_one, False]
        f_i_plus_one += f_i
        f_i = f_i_plus_one - f_i
