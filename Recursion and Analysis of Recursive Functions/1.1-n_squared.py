# No operations after recurcsion call
def n_squared_recursive_tail(n):
    if n > 0:
        n_squared = n ** 2
        print(n_squared)
        n_squared_recursive_tail(n-1)


def n_squared_iterative(n):
    while n > 0:
        n_squared = n ** 2
        print(n_squared)
        n -= 1


# No operations after base condition
def n_squared_recursive_head(n):
    if n > 0:
        n_squared_recursive_head(n-1)
        n_squared = n ** 2
        print(n_squared)


n = 5
n_squared_iterative(n)
n_squared_recursive(n)
n_squared_recursive_head(n)
