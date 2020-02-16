# DUBSTEP (6 KYU)
#
# Polycarpus works as a DJ in the best Berland nightclub, and he often uses dubstep music in his performance.
# Recently, he has decided to take a couple of old songs and make dubstep remixes from them.
#
# Let's assume that a song consists of some number of words (that don't contain WUB).
# To make the dubstep remix of this song, Polycarpus inserts a certain number of words "WUB"...
# 1) ...before the first word of the song (the number may be zero),
# 2) ...after the last word (the number may be zero), and
# 3) ...between words (at least one between any pair of neighbouring words),
# ...and then the boy glues together all the words, including "WUB", in one string and plays the song at the club.
#
# For example, a song with words "I AM X" CAN transform into a dubstep remix as...
# "WUBWUBIWUBAMWUBWUBX"
# ...and CANNOT transform into
# "WUBWUBIAMWUBX".
#
# Recently, Jonny has heard Polycarpus's new dubstep track, but since he isn't into modern music,
# he decided to find out what was the initial song that Polycarpus remixed.
# Help Jonny restore the original song.
#
# INPUT:
# The input consists of a single non-empty string, consisting only of uppercase English letters.
# The string's length doesn't exceed 200 characters.
#
# OUTPUT:
# Return the words of the initial song that Polycarpus used to make a dubsteb remix.
# Separate the words with a space.
#
# EXAMPLE:
# song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
#   # =>  WE ARE THE CHAMPIONS MY FRIEND

def song_decoder(song):
    newsong = song.split('WUB')
    newsong = [i for i in newsong if i != '']
    newsong = ' '.join(newsong)
    return newsong
