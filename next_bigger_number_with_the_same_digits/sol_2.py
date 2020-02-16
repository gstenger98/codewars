# This solution works super well when the digits are all or mostly unique. However, it is very
# slow for numbers like 9999999999, since there are many duplicate digits to go through.
# Make a new solution that solves this issue. (When you wrote this version, you knew in the back of your head
# that your duplicate-case methods were a bit of a shortcut.... Get rid of the make_unique stuff.)
#
# Also I forgot to save my first version, which is the follow-your-nose solution. Rewrite that one for practice.

def count_up(l):
    reversed_l = [l[len(l) - i - 1] for i in range(len(l))]
    reversed_l.append(0)
    reversed_l[0] += 1
    for i in range(len(l)):
        if reversed_l[i] > i:
            reversed_l[i] = 0
            reversed_l[i + 1] += 1
    if reversed_l[len(l)] != 0:
        return -1
    else:
        l = [reversed_l[len(l) - i - 1] for i in range(len(l))]
        return l

def simplified_form_as_list(n):
    n_list = list(map(float, n))
    temp_sorted_list = sorted(n_list)
    simplified_list = []
    for i in range(len(n)):
        value = str(temp_sorted_list.index(n_list[i]))
        simplified_list.append(value)
        del temp_sorted_list[int(value)]
    simplified_list = list(map(int, simplified_list))
    return simplified_list

def convert_back_to_normal(l, n):
    n_list = list(map(float, n))
    temp_sorted_list = sorted(n_list)
    simplified_list = []
    for i in range(len(l)):
        value = str(temp_sorted_list[l[i]])
        simplified_list.append(value)
        del temp_sorted_list[l[i]]
    simplified_list = list(map(float, simplified_list))
    # print(simplified_list)
    return simplified_list

def make_digits_unique(n):
    n_list = list(map(int, list(str(n))))
    temp_list = [-1.0 for x in n_list]
    for i in range(len(n_list)):
        for j in range(i + 1, len(n_list)):
            if n_list[i] == n_list[j]:
                temp_list[j] = n_list[j] + (j / 10)
        if temp_list[i] == -1.0:
            temp_list[i] = n_list[i]
    n_list = temp_list
    return n_list

def undo_make_digits_unique(n):
    answer = [str(int(x // 1)) for x in n]
    # print(answer)
    answer = int(''.join(answer))
    # print(answer)
    return answer

def next_bigger(n):
    print(n)
    m = make_digits_unique(n)
    # print(m)
    x = simplified_form_as_list(m)
    # print(x)
    foundanswer = False
    while not foundanswer:
        c = count_up(x)
        # print(c)
        if c == -1:
            print(-1)
            return -1
        x = c
        b = convert_back_to_normal(x, m)
        # print(b)
        a = undo_make_digits_unique(b)
        # print(a)
        if a > n:
            foundanswer = True
    print(a)
    return a

next_bigger(12)
next_bigger(513)
next_bigger(2017)
next_bigger(414)
next_bigger(144)
next_bigger(123456789)
next_bigger(1234567890)
next_bigger(9876543210)
next_bigger(9999999999)
next_bigger(1672938461)
next_bigger(1263947612)
