def linear_search(a, key):
    length = len(a)
    idx = 0
    while idx < length:
        if a[idx] == key:
            return idx
        idx += 1
    return -1


a = [1, 3, 5, 10, 13]
key = 5
print(linear_search(a, key))
