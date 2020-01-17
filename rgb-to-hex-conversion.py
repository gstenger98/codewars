# RGB TO HEX CONVERSION (5 KYU)
#
# The rgb() method is incomplete.
# Complete the method so that passing in RGB decimal values will result in a hexadecimal representation being returned.
# The valid decimal values for RGB are 0 - 255.
# Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.
#
# The following are EXAMPLES of expected output values:
# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3

def rgb(r, g, b):
    rgb_list = [r, g, b]
    rgb_list = [255 if i > 255 else 0 if i < 0 else i for i in rgb_list]

    rt = divmod(rgb_list[0],16)
    gt = divmod(rgb_list[1],16)
    bt = divmod(rgb_list[2],16)

    l = [str(rt[0]), str(rt[1]), str(gt[0]), str(gt[1]), str(bt[0]), str(bt[1])]
    l = [
        'A' if i == '10'
        else 'B' if i == '10'
        else 'B' if i == '11'
        else 'C' if i == '12'
        else 'D' if i == '13'
        else 'E' if i == '14'
        else 'F' if i == '15'
        else i for i in l
        ]

    s = ''.join(l)
    return s
