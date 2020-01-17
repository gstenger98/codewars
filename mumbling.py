# MUMBLING (KYU 7)
#
# This time no story, no theory. The examples below show you how to write function accum:
#
# EXAMPLES:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.

def accum(s):
    l = list(s)
    k = []
    for x in range(len(l)):
        k.append(l[x].upper() + x * l[x].lower())
    return "-".join(k)
