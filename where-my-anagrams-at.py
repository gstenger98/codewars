# WHERE MY ANAGRAMS AT? (5 KYU)
#
# What is an anagram?
# Well, two words are anagrams of each other if they both contain the same letters.
#
# For example:
# 'abba' & 'baab' == true
# 'abba' & 'bbaa' == true
# 'abba' & 'abbba' == false
# 'abba' & 'abca' == false
#
# Write a function that will find all the anagrams of a word from a list.
# You will be given two inputs a word and an array with words.
# You should return an array of all the anagrams or an empty array if there are none.
#
# For EXAMPLE:
# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []


def anagrams(word, words):
    sorted_word = ""
    sorted_word = sorted_word.join(sorted([letter for letter in word]))
    anagram_list = []
    for w in words:
        sorted_w = ""
        sorted_w = sorted_w.join(sorted([letter for letter in w]))
        if sorted_w == sorted_word:
            anagram_list.append(w)
    return anagram_list
