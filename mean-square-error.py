# MEAN SQUARE ERROR (5 KYU)
#
# Complete the function that...
# 1) accepts two integer arrays of equal length,
# 2) compares the value each member in one array to the corresponding member in the other,
# 3) squares the absolute value difference between those two values, and
# 4) returns the average of those squared absolute value difference between each member pair.
#
# EXAMPLES:
# [1, 2, 3], [4, 5, 6]              -->   9   because (9 + 9 + 9) / 3
# [10, 20, 10, 2], [10, 25, 5, -2]  -->  16.5 because (0 + 25 + 25 + 16) / 4
# [-1, 0], [0, -1]                  -->   1   because (1 + 1) / 2


def solution(array_a, array_b):
    return sum([((array_a[i] - array_b[i]) ** 2) / len(array_a) for i in range(len(array_a))])
