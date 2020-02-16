# SIMPLE FUN #68: PALINDROME REARRANGING (7 KYU)
#
# TASK:
# Given a string s, find out if its characters can be rearranged to form a palindrome.
#
# EXAMPLE:
# For s = "aabb", the output should be true.
# (It outputs true because we can rearrange "aabb" to make "abba", which is a palindrome.)
#
# INPUT:
# - string s
# - A string consisting of lowercase English letters.
# - CONSTRAINTS: 4 ≤ inputString.length ≤ 50.
#
# OUTPUT:
# - a boolean value
# - true if the characters of the inputString can be rearranged to form a palindrome, false otherwise.


def palindrome_rearranging(s):
    letter_count_dict = {}
    for _ in s:
        if _ not in letter_count_dict:
            letter_count_dict[_] = 0
        letter_count_dict[_] += 1
        letter_count_dict[_] = letter_count_dict[_] % 2
    if sum(letter_count_dict.values()) > 1:
        return False
    return True
