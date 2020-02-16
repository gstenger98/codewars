# ALPHABETICAL ADDITION (7 KYU)
#
# Your task is to add up letters to one letter.
# The function will be given a variable amount of arguments, each one being a letter to add.
#
# NOTES:
# Letters will always be lowercase.
# Letters can overflow (see second to last example of the description)
# If no letters are given, the function should return 'z'
#
# EXAMPLES:
# add_letters('a', 'b', 'c') = 'f'
# add_letters('a', 'b') = 'c'
# add_letters('z') = 'z'
# add_letters('z', 'a') = 'a'
# add_letters('y', 'c', 'b') = 'd' # notice the letters overflowing
# add_letters() = 'z'

def add_letters(*letters):
    # Instead of typing the letters alphabetically one-by-one, I just ran my finger along the keys for each of the three rows of letters. Then I sorted them.
    alphabet = sorted(list('qwertyuiopasdfghjklzxcvbnm'))

    # Now I use a for-loop and index() to sum up the values of the letters-as-numbers.
    sum = 0
    for _ in letters:
        sum += alphabet.index(_) + 1

    # Converting back to a letter....
    answer_letter = alphabet[(sum - 1) % 26]
    return answer_letter
