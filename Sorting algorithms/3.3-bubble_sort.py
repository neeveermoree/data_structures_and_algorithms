def bubble_sort(arr):
    length = len(arr)
    sort_end_idx = length
    while sort_end_idx > 1:
        arr[:sort_end_idx] = sort_pass(arr[:sort_end_idx])
        sort_end_idx -= 1
    return arr


def sort_pass(arr):
    length = len(arr)
    for i in range(length-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


# 0 -1 3 6 2 -1 4 8
# -1 0
#    0 3
#      3 6
#        2 6
#          -1 6
#             4 6
#               6 8

# -1 0 3 2 -1 4 6 8

arr = [0, -1, 3, 6, 2, -1, 4, 8]
print(bubble_sort(arr))
