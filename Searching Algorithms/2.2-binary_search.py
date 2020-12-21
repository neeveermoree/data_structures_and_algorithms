def binary_search_iterative(arr, key):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (r - l // 2) + l
        if arr[m] == key:
            return m
        elif arr[m] > key:
            r = m - 1
        else:
            l = m + 1
    return -1


def binary_search_recursive(arr, start, end, key):
    if start > end:
        return -1
    m = (end + start) // 2
    if arr[m] == key:
        return m
    elif arr[m] > key:
        end = m - 1
        return binary_search_recursive(arr, start, end, key)
    else:
        start = m + 1
        return binary_search_recursive(arr, start, end, key)    


a = [1, 2, 5, 7, 10, 12]
print(binary_search_recursive(a, 0, len(a)-1, -1))
