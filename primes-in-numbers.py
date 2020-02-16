# PRIMES IN NUMBERS (5 KYU)
#
# Given a positive number n > 1 find the prime factor decomposition of n.
# The result will be a string with the following form:
# "(p1**n1)(p2**n2)...(pk**nk)",
# with the p(i) in increasing order and n(i) empty if n(i) is 1.
#
# EXAMPLE: n = 86240 should return "(2**5)(5)(7**2)(11)"

def primeFactors(n):
    l = []
    for i in range(2, int(n) + 1):
        if n / i == n // i:
            is_finished = False
            count = 1
            while is_finished is False:
                l.append(i)
                n /= i
                if n / i != n // i:
                    is_finished is True
                    if count == 1:
                        return'(' + str(i) + ')' + primeFactors(n)
                    else:
                        return'(' + str(i) + '**' + str(count) + ')' + primeFactors(n)
                count += 1
    l = ''
    return l
