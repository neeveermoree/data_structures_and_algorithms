def inserion_sort(arr):
    length = len(arr)
    for i in range(1, length):
        for j in range(i-1, -1, -1):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr


def inserion_sort_more_efficent(arr):
    length = len(arr)
    for i in range(1, length):
        cur = arr[i]
        cur_idx = i
        while cur_idx > 0 and cur < arr[i]:
            arr[cur_idx] = arr[cur_idx-1]
            cur_idx -= 1
        arr[cur_idx] = cur
    return arr


# 1 2 0 -3 5 7 2 9 6
# !
# 1 2 0 -3 5 7 2 9 6
# ! !
# 1 2 0 -3 5 7 2 9 6
# ! ! !
# 1 0 2 -3 5 7 2 9 6
# 0 1 2 -3 5 7 2 9 6
# ! ! ! !
# 0 1 -3 2 5 7 2 9 6
# 0 -3 1 2 5 7 2 9 6
# -3 0 1 2 5 7 9 2 6


arr = [1, 2, 0, -3, 5, 7, 2, 9, 6]
print(inserion_sort(arr))
print(inserion_sort_more_efficent(arr))
