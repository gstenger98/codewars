# VALID BRACES (6 KYU)
#
# Write a function that takes a string of braces, and determines if the order of the braces is valid.
# It should return true if the string is valid, and false if it's invalid.
#
# All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.
#
# What is considered Valid?
# A string of braces is considered valid if all braces are matched with the correct brace.
#
# Examples
# "(){}[]"   =>  True
# "([{}])"   =>  True
# "(}"       =>  False
# "[(])"     =>  False
# "[({})](]" =>  False

def validBraces(str):
    if len(str) % 2 == 1:
        return False
    s = str
    s = s.replace('()','')
    s = s.replace('[]','')
    s = s.replace('{}','')
    if s == '':
        return True
    if len(str) > len(s):
        return validBraces(s)
    return False
