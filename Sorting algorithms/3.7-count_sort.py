def count_sort(arr):
    length = len(arr)
    max_val = -1
    for i in range(length):
        if arr[i] > max_val:
            max_val = arr[i]
    tmp_arr = [0] * (max_val + 1)
    for i in range(length):
        tmp_arr[arr[i]] += 1
    arr_idx = 0
    for i in range(max_val+1):
        occurence_amount = tmp_arr[i]
        while occurence_amount > 0:
            arr[arr_idx] = i
            arr_idx += 1
            occurence_amount -= 1


arr = [3, 6, 2, 1, 3]
count_sort(arr)
print(arr)
