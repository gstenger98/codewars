# SIMPLE ENCRYPTION #1 - ALTERNATING SPLIT (6 KYU)
#
# For building the encrypted string:
# Take every 2nd char from the string, then the other chars, that are not every
# 2nd char, and concat them as new String.
#
# Do this n times!
#
# EXAMPLES:
# "This is a test!", 1 -> "hsi  etTi sats!"
# "This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
# Write two methods:
#
# def encrypt(text, n)
# def decrypt(encrypted_text, n)
# For both methods:
# If the input-string is null or empty return exactly this value!
# If n is <= 0 then return the input text.
#
# This kata is part of the Simple Encryption Series:
# Simple Encryption #1 - Alternating Split
# Simple Encryption #2 - Index-Difference
# Simple Encryption #3 - Turn The Bits Around
# Simple Encryption #4 - Qwerty
#
# Have fun coding it and please don't forget to vote and rank this kata! :-)

def decrypt(encrypted_text, n):
    if n <= 0 or encrypted_text == '' or encrypted_text == None:
        return encrypted_text
    right_list_str = encrypted_text[len(encrypted_text) // 2:]
    left_list_str = encrypted_text.replace(right_list_str, '')
    decrypted_list = []
    isright = True
    for i in range(len(encrypted_text)):
        if isright == True:
            decrypted_list.append(right_list_str[i // 2])
        else:
            decrypted_list.append(left_list_str[i // 2])
        isright = not isright
    decrypted_text = ''.join(decrypted_list)
    return decrypt(decrypted_text, n - 1)


def encrypt(text, n):
    if n <= 0 or text == '' or text == None:
        return text
    left_list = []
    right_list = []
    isleft = True
    for _ in text:
        if isleft == True:
            left_list.append(_)
        else:
            right_list.append(_)
        isleft = not isleft
    left_list_str = ''.join(left_list)
    right_list_str = ''.join(right_list)
    encrypted_text = right_list_str + left_list_str
    return encrypt(encrypted_text, n - 1)
