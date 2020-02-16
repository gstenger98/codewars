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
    return code_list, bases_list

def next_bigger(n):
    print(n)
    r = undo_n_code_and_n_bases(count_up_by_one_unit(n_code_and_n_bases(n)), n)
    print(r)
    return(r)
