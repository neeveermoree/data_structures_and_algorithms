def sum_n_numbers_const(n):
    return int(n * (n + 1) / 2)


def sum_n_numbers_iterative(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s


def sum_n_numbers_recursive(n):
    if n == 1:
        return 1
    return n + sum_n_numbers_recursive(n-1)


n = 7
print(sum_n_numbers_const(n))
print(sum_n_numbers_iterative(n))
print(sum_n_numbers_recursive(n))
