# POTION CLASS 101 (6 KYU)
#
# DESCRIPTION:
# This is your first potion class in Hogwarts and professor gave you a homework to
# figure out what color potion will turn into if he'll mix it with some other potion.
# All potions have some color that written down as RGB color from [0, 0, 0] to [255, 255, 255].
# To make task more complicated teacher will do few mixing and after will ask you for final color.
# Besides color you also need to figure out what volume will have potion after final mix.
#
# TASK:
# Based on your programming background you managed to figure that after mixing two
# potions colors will mix as if mix two RGB colors. For example, if you'll mix potion that
# have color [255, 255, 0] and volume 10 with one that have color [0, 254, 0] and volume 5,
# you'll get new potion with color [170, 255, 0] and volume 15. So you decided to
# create a class Potion that will have two properties: color (a list with 3 integers)
# and volume (a number), and one method mix that will accept another Potion and return a mixed Potion.
#
# EXAMPLE:
# felix_felicis       =  Potion([255, 255, 255],  7)
# shrinking_solution  =  Potion([ 51, 102,  51], 12)
# new_potion          =  felix_felicis.mix(shrinking_solution)
#
# new_potion.color   ==  [127, 159, 127]
# new_potion.volume  ==  19
# 
# NOTE: Use ceiling when calculating the resulting potion's color.

class Potion:
    def __init__(self, color, volume):
        self.color = color
        self.volume = volume

    def mix(self, other):
        color_a = self.color
        color_b = other.color
        volume_a = self.volume
        volume_b = other.volume

        weighted_a = [_ * volume_a for _ in color_a]
        weighted_b = [_ * volume_b for _ in color_b]

        weighted_final = [weighted_a[_] + weighted_b[_] for _ in range(len(weighted_a))]
        rescaled_final_with_integer_approx = [(-1) * (((-1) * _) // (volume_a + volume_b)) for _ in weighted_final]

        final_color = tuple(rescaled_final_with_integer_approx)
        final_volume = int(volume_a + volume_b)

        new_potion = Potion(final_color, final_volume)
        return new_potion
