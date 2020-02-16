# BALANCED NUMBER SPECIAL NUMBERS SERIES #1 (7 KYU)
#
# DEFINITION:
# A balanced number is the number that the sum of all digits to the left of the middle digit(s)
# and the sum of all digits to the right of the middle digit(s) are equal.
#
# TASK:
# Given a number, find if it is balanced or not.

def balanced_num(number):
    number_list = list(str(number))
    if len(str(number)) % 2 == 0:
        left_sum_list_range = int((len(str(number)) / 2) - 1)
        left_sum_list = [int(number_list[_]) for _ in range(left_sum_list_range)]
        right_sum_list = [int(number_list[_]) for _ in range(left_sum_list_range + 2, len(str(number)))]
    else:
        left_sum_list_range = int((len(str(number)) - 1) / 2)
        left_sum_list = [int(number_list[_]) for _ in range(left_sum_list_range)]
        right_sum_list = [int(number_list[_]) for _ in range(left_sum_list_range + 1, len(str(number)))]
    left_sum = sum(left_sum_list)
    right_sum = sum(right_sum_list)
    if left_sum == right_sum:
        return 'Balanced'
    return 'Not Balanced'
