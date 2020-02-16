# This was too slow for numbers above 10,000. The problem wanted me to be able to calculate up to 2,000,000.

def fib(n):
    # print(n)
    fib_matrix = [[1, 1], [1, 0]]
    # print(fib_matrix)
    nth_fib_matrix = [[1, 0], [0, 1]]
    for _ in range(abs(n)):
        # print(nth_fib_matrix)
        future_nth_fib_matrix = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    future_nth_fib_matrix[i][j] += fib_matrix[i][k] * nth_fib_matrix[k][j]
        nth_fib_matrix = future_nth_fib_matrix
    # print(n)
    # print(nth_fib_matrix[0][1])
    answer = nth_fib_matrix[0][1]
    if n != abs(n):
        if n % 2:
            answer *= -1
        answer *= -1
    print(answer)
    return answer
