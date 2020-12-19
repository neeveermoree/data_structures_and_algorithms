def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n-1)


def factorial_iterative(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans


n = 4
print(factorial_recursive(n))
print(factorial_iterative(n))
