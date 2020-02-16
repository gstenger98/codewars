# DUPLICATE ENCODER (6 KYU)
#
# The goal of this exercise is to convert a string to a new string where each
# character in the new string is "(" if that character appears only once in
# the original string, or ")" if that character appears more than once in the original string.
# Ignore capitalization when determining if a character is a duplicate.
#
# EXAMPLES:
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("

def duplicate_encode(word):
    word = word.lower()
    sorted_list = sorted(list(word))
    unique_list = list(set(word))

    for _ in unique_list:
        sorted_list.remove(_)

    unique_list_of_duplicates = list(set(sorted_list))
    answer = ''

    for _ in word:
        if _ in unique_list_of_duplicates:
            answer += ')'
        else:
            answer += '('

    return answer
