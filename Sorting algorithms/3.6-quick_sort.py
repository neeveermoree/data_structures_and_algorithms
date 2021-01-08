# left starting idx inplace
# right ending idx + 1 (aka arr length)
def quick_sort(arr, left, right):
    if right - left > 1:
        pivot_idx = find_pivot_idx(arr, left, right)
        quick_sort(arr, left, pivot_idx)
        quick_sort(arr, pivot_idx+1, right)


def find_pivot_idx(arr, left, right):
    pivot_idx = left
    pivot_val = arr[pivot_idx]
    
    i = left
    j = right - 1

    while i <= j:
        if arr[i] > pivot_val:
            if arr[j] < pivot_val:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
            else:
                j -= 1
        else:
            i += 1
    if arr[j] < pivot_val:
        arr[j], arr[pivot_idx] = arr[pivot_idx], arr[j]
    return j


arr = [54, 78, 63, 92, 45, 86, 15, 28, 37]
quick_sort(arr, 0, len(arr))
print(arr)
