# SIMPLE PIG LATIN (5 KYU)
#
# Move the first letter of each word to the end of it, then add "ay" to the end of the word.
# Leave punctuation marks untouched.
#
# EXAMPLES:
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    return ''.join([_[1:] + _[0] + 'ay ' if _.isalnum() else _ for _ in text.split(' ')]).strip()
