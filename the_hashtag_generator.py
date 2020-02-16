# THE HASHTAG GENERATOR (5 KYU)
#
# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!
#
# Here's the deal:
# - It must start with a hashtag (#).
# - All words must have their first letter capitalized.
# - If the final result is longer than 140 chars it must return false.
# - If the input or the result is an empty string it must return false.
#
# EXAMPLES:
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false


def generate_hashtag(s):
    if s == '':
        return False
    if len(s) > 140:
        return False
    hash_list = s.split(' ')
    cap_hash_list = []
    for l in hash_list:
        cap_hash_list.append(l.capitalize())
    hash_word = ''
    for k in cap_hash_list:
        hash_word += k
    hash_word = '#' + hash_word
    print(hash_word)
    return hash_word
