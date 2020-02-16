# NEXT BIGGER NUMBER WITH THE SAME DIGITS (4 KYU)
#
# You have to create a function that takes a positive integer number and returns
# the next bigger number formed by the same digits:
#
# 12 ==> 21
# 513 ==> 531
# 2017 ==> 2071
#
# If no bigger number can be composed using those digits, return -1:
#
# 9 ==> -1
# 111 ==> -1
# 531 ==> -1

def undo_codifier(updated_codified_n_and_n):
    if updated_codified_n_and_n == -1:
        return -1

    updated_codified_n = updated_codified_n_and_n[0]
    n = updated_codified_n_and_n[1]

    n_list = [int(_) for _ in str(n)]
    unique_digits_in_n = sorted(list(set(n_list)))

    for i in range(len(updated_codified_n)):
        n_list[i] = unique_digits_in_n[updated_codified_n[i]]

    n_list = int(''.join(str(_) for _ in n_list))
    return n_list

def update_codified_ending(end_of_new_codified_n_and_code_list_and_n):
    if end_of_new_codified_n_and_code_list_and_n == -1:
        return -1

    end_of_new_codified_n = end_of_new_codified_n_and_code_list_and_n[0]
    code_list = end_of_new_codified_n_and_code_list_and_n[1]
    n = end_of_new_codified_n_and_code_list_and_n[2]

    updated_codified_n = code_list[:len(code_list) - len(end_of_new_codified_n)]
    updated_codified_n.extend(end_of_new_codified_n)

    return updated_codified_n, n

def climb_down_codified_tree(digit_counter_and_new_digit_and_code_list_and_n):
    if digit_counter_and_new_digit_and_code_list_and_n == -1:
        return -1

    digit_counter = digit_counter_and_new_digit_and_code_list_and_n[0]
    new_digit = digit_counter_and_new_digit_and_code_list_and_n[1]
    code_list = digit_counter_and_new_digit_and_code_list_and_n[2]
    n = digit_counter_and_new_digit_and_code_list_and_n[3]
    end_of_new_codified_n = [new_digit]

    for i in range(len(digit_counter)):
        temp_count = digit_counter[i]
        while temp_count > 0:
            end_of_new_codified_n.append(i)
            temp_count -= 1

    return end_of_new_codified_n, code_list, n

def climb_up_codified_tree(code_list_and_n):
    code_list = code_list_and_n[0]
    n = code_list_and_n[1]

    digit_counter = [0 * _ for _ in code_list]
    reversed_code_list = [_ for _ in code_list[::-1]]
    found_open_right_branch = False
    current_digit_index = 0

    while not found_open_right_branch:
        current_digit = reversed_code_list[current_digit_index]
        digit_counter[current_digit] += 1
        for i in range(current_digit + 1, len(digit_counter)):
            if digit_counter[i] > 0:
                found_open_right_branch is True
                digit_counter[i] -= 1
                new_digit = i
                return digit_counter, new_digit, code_list, n
        current_digit_index += 1
        if current_digit_index == len(reversed_code_list):
            return -1

def codify(n):
    n_list = [int(_) for _ in str(n)]
    unique_digits_in_n = sorted(list(set(n_list)))
    code_list = []

    for i in range(len(n_list)):
        indx = unique_digits_in_n.index(n_list[i])
        code_list.append(indx)

    return code_list, n

def next_bigger(n):
    print(n)
    result = undo_codifier(update_codified_ending(climb_down_codified_tree(climb_up_codified_tree(codify(n)))))
    print(result)
    return result

next_bigger(3981)
next_bigger(128350)
next_bigger(100350)
next_bigger(120150)
next_bigger(9876543210)
next_bigger(59884848459853)
