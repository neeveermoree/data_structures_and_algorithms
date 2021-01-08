def radix_sort(arr):
    max_val = -1
    for val in arr:
        if max_val < val:
            max_val = val
    digits = len(str(max_val))
    for dig in range(digits):
        tmp_arr = [[] for _ in range(10)]  #10 digits
        for val in arr:
            str_val = str(val)
            if dig < len(str_val):
                val_digit = int(str_val[::-1][dig])
            else:
                val_digit = 0
            tmp_arr[val_digit].append(val)
        arr_c = 0
        for d in range(10):
            l = len(tmp_arr[d]) 
            while l > 0:
                arr[arr_c] = tmp_arr[d][::-1][l-1]
                arr_c += 1
                l -= 1


arr = [334, 112, 15, 3551, 415]
print(arr)
radix_sort(arr)
print(arr)
