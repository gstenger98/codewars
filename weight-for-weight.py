# WEIGHT FOR WEIGHT (5 KYU)
#
# My friend John and I are members of the "Fat to Fit Club (FFC)".
# John is worried because each month a list with the weights of members is published,
# and each month he is the last on the list which means he is the heaviest.
#
# I am the one who establishes the list so I told him:
# "Don't worry any more, I will modify the order of the list".
# It was decided to attribute a "weight" to numbers.
# The weight of a number will be from now on the sum of its digits.
#
# For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99.
# Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?
#
# EXAMPLE:
# "56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes:
# "100 180 90 56 65 74 68 86 99"
#
# When two numbers have the same "weight", let us class them as if they were strings (alphabetical ordering) and not numbers:
# 100 is before 180 because its "weight" (1) is less than the one of 180 (9),
# and 180 is before 90 since, having the same "weight" (9), it comes before as a string.
#
# All numbers in the list are positive numbers and the list can be empty.



def dig_sum(num):
    # Here we remove the highest digit from num, adding this digit to count each time.
    i = int(num)
    count = 0
    simplified = False
    while simplified is False:
        if len(str(i)) == 1:
            simplified = True
        initial_i = i
        first_digit = i // (10 ** (len(str(i)) - 1))
        remaining_digits = i % (10 ** (len(str(i)) - 1))
        count += first_digit
        i = remaining_digits
    return count

def order_weight(strng):
    if strng == "":
        return ""
    # Turn strng into a list, and sort 'alphabetically' (even though they're integers).
    l = sorted(strng.split(" "))
    # Create a set to store dig_sum's. Create a dummy list for later.
    s = set()
    t = []
    # Add dig_sum's to set.
    for i in l:
        count = dig_sum(i)
        s.add(count)
    # Convert the set of dig_sum's into a list, and sort numerically.
    ll = sorted([_ for _ in s])
    # Go through you set-turned-into-list of dig_sum's, and append elements of
    # your strng-turned-into-list that have the appropriate dig_sum.
    for j in ll:
        for k in l:
            if dig_sum(k) == j:
                t.append(str(k))
    # Now you're done.
    return " ".join(t)

# My dig_sum method is pretty janky -- the simpler way to perform a dig_sum is:
#
# def dig_sum(num):
#     return(sum(int(dig) for dig in num), num)
#
# ... and as it turns out, my order_weight method is janky as well lol. A more
# direct version of order_weight is:
#
# def order_weight(strng):
#     t = sorted(strng.split(' '), key=dig_sum)
#     return ' '.join(t)
