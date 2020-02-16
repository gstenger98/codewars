# INTRO TO ART (6 KYU)
#
# Help prepare for the entrance exams to art school.
# It is known in advance that this year, the school chose the symmetric letter “W” as
# the object for the image, and the only condition for its image is only the size that
# is not known in advance, so as training, you need to come up with a way that accurately depicts the object.
#
# Write a function that takes an integer and returns a list of strings with a line-by-line image of the object.
#
# Below is an EXAMPLE function:
#
# get_w(3) # should return:
# [
# '*   *   *',
# ' * * * * ',
# '  *   *  '
# ]
#
# get_w(5) # should return:
# [
# '*       *       *',
# ' *     * *     * ',
# '  *   *   *   *  ',
# '   * *     * *   ',
# '    *       *    '
# ]

def get_w(height):
    if height < 2:
        return []
    w_list = []
    for i in range(height):
        initial_block = ' ' * i + '*' + ' ' * (height - 1 - i)
        flipped_block = initial_block[:-1] + initial_block[::-1]
        complete_block = flipped_block[:-1] + flipped_block[::-1]
        w_list.append(complete_block)
    return w_list
