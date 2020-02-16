# HELP BOB COUNT LETTERS AND DIGITS (7 KYU)
#
# Bob is a lazy man.
# He needs you to create a method that can determine how many letters and digits are in a given string.
#
# EXAMPLE:
# "hel2!lo" --> 6
# "wicked .. !" --> 6
# "!?..A" --> 1

def count_letters_and_digits(s):
    l = []
    for _ in s:
        bool_alpha = _.isalpha()
        bool_num = _.isnumeric()
        if bool_alpha or bool_num:
            l.append(_)
    answer = len(l)
    return answer
