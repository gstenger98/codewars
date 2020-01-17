# Write Number in Expanded Form (6 KYU)
#
# You will be given a number and you will need to return it as a string in Expanded Form. For example:
#
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
#
# NOTE: All numbers will be whole numbers greater than 0.

def expanded_form(num):
    l = list(str(num))
    k = [len(l) - i - 1 for i in range(len(l))]
    j = list(map(lambda x,y : str(int(x) * 10 ** int(y)), l, k))

    i = ' + '.join(j)
    i = i.replace(' + 0','')

    return i
