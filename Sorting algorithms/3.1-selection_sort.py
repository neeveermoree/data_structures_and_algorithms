def selection_sort(arr):
    length = len(arr)
    for i in range(length-1):
        min_value_idx = find_minimum_value(arr[i:])
        arr[i], arr[i+min_value_idx] = arr[i+min_value_idx], arr[i]
    return arr


def find_minimum_value(arr):
    length = len(arr)
    min_value_idx = 0
    min_value = arr[min_value_idx]
    idx = 1
    while idx < length:
        if arr[idx] < min_value:
            min_value_idx = idx
            min_value = arr[min_value_idx]
        idx += 1
    return min_value_idx


def selection_sort_rec(arr):
    if len(arr) == 1:
        return arr
    min_value_idx = find_minimum_value(arr)
    arr[0], arr[min_value_idx] = arr[min_value_idx], arr[0]
    return [arr[0]] + selection_sort_rec(arr[1:])


# 1 4 2 9 -1 9 13 2
# 1) find min
# -1
# 2) replace -1 with element at first position
# -1 4 2 9 1 9 13 2
# 3) same for array without min element

arr = [1, 4, 2, 9, -1, 9, 13, 2]
print(selection_sort(arr))
print(selection_sort_rec(arr))

arr = [3, 5, 8, 9, 6, 2]
print(selection_sort(arr))
print(selection_sort_rec(arr))
