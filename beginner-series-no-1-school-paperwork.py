# BEGINNER SERIES #1 SCHOOL PAPERWORK (8 KYU)
#
# Your classmates asked you to copy some paperwork for them. You know that there
# are 'n' classmates and the paperwork has 'm' pages.
#
# Your task is to calculate how many blank pages do you need.
#
# EXAMPLE:
# paperwork(5, 5) == 25
# Note! if n or m < 0 return 0! Waiting for translations and Feedback! Thanks!

def paperwork(n, m):
    return n * m if n == abs(n) and m == abs(m) else 0
