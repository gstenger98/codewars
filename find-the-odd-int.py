# FIND THE ODD INT (6 KYU)
#
# Given an array, find the integer that appears an odd number of times.
#
# There will always be only one integer that appears an odd number of times.


def find_it(seq):
    if len(set(seq)) == 1:
        return seq[0]
    a = sorted(seq)
    index = 0
    while 1 != 2:
        if a[index] != a[index + 1]:
            return a[index] if index % 2 == 0 else find_it(a[index + 1:])
        index += 1
