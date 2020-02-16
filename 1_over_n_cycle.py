# 1/n-CYCLE (6 KYU)
#
# Let be n an integer prime with 10 e.g. 7.
# 1/7 = 0.142857 142857 142857 ....
# We see that the decimal part has a cycle: 142857. The length of this cycle is 6.
#
# In the same way:
# 1/11 = 0.09 09 09 .... Cycle length is 2.
#
# TASK:
# Given an integer n (n > 1), the function cycle(n) returns the length of the cycle
# if n and 10 are coprimes, otherwise returns -1.
#
# EXAMPLES:
# cycle(5) = -1
# cycle(13) = 6 -> 0.076923 076923 0769
# cycle(21) = 6 -> 0.047619 047619 0476
# cycle(27) = 3 -> 0.037 037 037 037 0370
# cycle(33) = 2 -> 0.03 03 03 03 03 03 03 03
# cycle(37) = 3 -> 0.027 027 027 027 027 0
# cycle(94) = -1
# cycle(22) = -1 since 1/22 ~ 0.0 45 45 45 45 ...

import math

def divisors(n):
    d_list = []
    for i in range(2, int(math.sqrt(n) + 1)):
        if (n / i) == int(n / i):
            d_list.append(i)
            d_list.append(int(n / i))
    d_list.append(n)
    d_list = sorted(d_list)
    return d_list

def primedivisors(n):
    d_list = divisors(n)
    p_list = []
    for i in d_list:
        if len(divisors(i)) == 1:
            p_list.append(i)
    return p_list

def divisorcheck(n,m):
    d_list = divisors(n)
    for q in d_list:
        if (10 ** q) % m == 1:
            return q
    return n

def phi_ifier(n):
    phi_n = n
    p_list = primedivisors(n)
    if not p_list:
        phi_n = int(n * (1 - (1 / n)))
        return phi_n
    for p in p_list:
        phi_n *= (1 - (1 / p))
    phi_n = int(phi_n)
    return phi_n

def cycle(n):
    if n % 5 == 0 or n % 2 == 0:
        return -1
    if n < 10:
        return 1
    answer = divisorcheck(phi_ifier(n),n)
    return answer
