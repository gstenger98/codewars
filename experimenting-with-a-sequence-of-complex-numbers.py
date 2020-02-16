# EXPERIMENTING WITH A SEQUENCE OF COMPLEX NUMBERS (6 KYU)
#
# Consider the sequence S(n, z) = (1 - z)(z + z**2 + z**3 + ... + z**n) where z is
# a complex number and n a positive integer (n > 0).
#
# When n goes to infinity and z has a correct value (ie z is in its domain of
# convergence D), S(n, z) goes to a finite limit lim depending on z.
#
# Experiment with S(n, z) to guess the domain of convergence Dof S and lim value when z is in D.
#
# Then determine the smallest integer n such that abs(S(n, z) - lim) < eps where
# eps is a given small real number and abs(Z) is the modulus or norm of the complex number Z.
#
# Call f the function f(z, eps) which returns n. If z is such that S(n, z) has no
# finite limit (when z is outside of D) f will return -1.
#
# EXAMPLES:
# I is a complex number such as I * I = -1 (sometimes written i or j).
#
# f(0.3 + 0.5 * I, 1e-4) returns 17
# f(30 + 5 * I, 1e-4) returns -1
#
# NOTE:
# You pass the tests if abs(actual - exoected) <= 1

def f(z, eps):
    if abs(z) > 1:
        return -1
    n = 0
    isfinished = False
    while isfinished == False:
        n += 1
        temp_value = z ** n
        if abs(temp_value) < eps:
            isfinished = True
    return n
