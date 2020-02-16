def n_code_reducer(n_code, n_bases):
    reversed_n_code = [_ for _ in n_code[::-1]]
    reversed_n_bases = [_ for _ in n_bases[::-1]]

    for i in range(len(n_code) - 1):
        current_n_code_digit = reversed_n_code[i]
        next_n_code_digit = reversed_n_code[i + 1]
        current_n_base = reversed_n_bases[i]

        next_n_code_digit += current_n_code_digit // current_n_base
        current_n_code_digit = current_n_code_digit % current_n_base

        reversed_n_code[i + 1] = next_n_code_digit
        reversed_n_code[i] = current_n_code_digit

    if reversed_n_code[len(n_code) - 1] >= reversed_n_bases[len(n_code) - 1]:
        final_n_code_digit = reversed_n_code[len(n_code) - 1] // reversed_n_bases[len(n_code) - 1]
        second_to_last_n_code_digit = reversed_n_code[len(n_code) - 1] % reversed_n_bases[len(n_code) - 1]

        reversed_n_code.append(final_n_code_digit)
        reversed_n_code[len(n_code) - 1] = second_to_last_n_code_digit

    count = 0
    for i in range(len(reversed_n_code) - 1):
        if reversed_n_code[i] == reversed_n_code[len(reversed_n_code) - 1]:
            count += 1
    reversed_n_bases.append(count)

    n_code = [_ for _ in reversed_n_code[::-1]]
    n_bases = [_ for _ in reversed_n_bases[::-1]]

    return n_code, n_bases


def undo_n_code_and_n_bases(n_code, original_n):
    if n_code == -1:
        return -1

    n_list = [int(_) for _ in str(original_n)]
    sorted_n_list = sorted(n_list)

    undo_n_code_list = []

    for i in range(len(n_code)):
        current_n_code_digit = n_code[i]
        undo_current_n_code_digit = sorted_n_list.pop(current_n_code_digit)
        undo_n_code_list.append(undo_current_n_code_digit)

    answer = int(''.join(list(map(str,undo_n_code_list))))
    return answer

def count_up_by_one_unit(n_code_and_n_bases):
    n_code = n_code_and_n_bases[0]
    n_bases = n_code_and_n_bases[1]

    reversed_n_code = [_ for _ in n_code[::-1]]
    reversed_n_bases = [_ for _ in n_bases[::-1]]

    reversed_n_code[0] += 1

    for i in range(len(n_code) - 1):
        current_n_code_digit = reversed_n_code[i]
        next_n_code_digit = reversed_n_code[i + 1]
        current_n_base = reversed_n_bases[i]

        if current_n_code_digit == current_n_base:
            next_n_code_digit += 1
            current_n_code_digit = 0

        reversed_n_code[i + 1] = next_n_code_digit
        reversed_n_code[i] = current_n_code_digit

    if reversed_n_code[len(n_code) - 1] == reversed_n_bases[len(n_code) - 1]:
        return -1

    n_code = [_ for _ in reversed_n_code[::-1]]
    n_bases = [_ for _ in reversed_n_bases[::-1]]
    print(n_code)
    return n_code

def n_code_and_n_bases(n):
    n_list = [int(_) for _ in str(n)]
    sorted_n_list = sorted(n_list)
    bases_list = []
    code_list = []
    for i in range(len(n_list)):
        current_digit = n_list[i]

        current_digit_base = len(set(sorted_n_list))
        bases_list.append(current_digit_base)

        current_digit_code = sorted_n_list.index(current_digit)
        code_list.append(current_digit_code)

        sorted_n_list.remove(current_digit)
    print(code_list)
    print(bases_list)
    code_list, bases_list = n_code_reducer(code_list, bases_list)
    print(code_list)
    print(bases_list)
    return code_list, bases_list

def next_bigger(n):
    print(n)
    r = undo_n_code_and_n_bases(count_up_by_one_unit(n_code_and_n_bases(n)), n)
    print(r)
    return(r)

# next_bigger(3981)
# next_bigger(128350)
# next_bigger(100350)
# next_bigger(120150)
# next_bigger(9876543210)

next_bigger(59884848459853)
# The problem is the number 59884848459853 is that its n_code is not in reduced notation.
# I'm going to make a n_code reducer now. I can use it in my count_up_by_one_unit method.
# This seems to be the wrong approach....
