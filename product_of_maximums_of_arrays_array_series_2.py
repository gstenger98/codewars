# PRODUCT OF MAXIMUMS OF ARRAYS (ARRAY SERIES #2) (7 KYU)
#
# Task
# Given an array/list [] of integers, find the product of the k maximal numbers.
#
# NOTES
# - Array/list size is at least 3.
# - Array/list's numbers will be mixture of positives, negatives and zeros.
# - Repetition of numbers in the array/list could occur.
#
# EXAMPLES (Input >> Output):
# - maxProduct ({4, 3, 5}, 2) ==>  return (20)
#     - Explanation:
#     - Since the size (k) equal 2 , then the subsequence of size 2 whose gives product of maxima is 5 * 4 = 20.
# - maxProduct ({8, 10 , 9, 7}, 3) ==>  return (720)
#     - Explanation:
#     - Since the size (k) equal 3 , then the subsequence of size 2 whose gives product of maxima is 8 * 9 * 10 = 720.
# - maxProduct ({10, 8, 3, 2, 1, 4, 10}, 5) ==> return (9600)
#     - Explanation:
#     - Since the size (k) equal 5 , then the subsequence of size 2 whose gives product of maxima is 10 * 10 * 8 * 4 * 3 = 9600.
# - maxProduct ({-4, -27, -15, -6, -1}, 2) ==> return (4)
#     - Explanation:
#     - Since the size (k) equal 2 , then the subsequence of size 2 whose gives product of maxima is -4 * -1 = 4.
# - maxProduct ({10, 3, -1, -27} , 3)  return (-30)
#     - Explanation:
#     - Since the size (k) equal 3 , then the subsequence of size 2 whose gives product of maxima is 10 * 3 * -1 = -30.



def max_product(lst, n_largest_elements):
    product = 1
    lst = sorted(lst)
    for _ in lst[-n_largest_elements:]:
        product *= _
    return product
