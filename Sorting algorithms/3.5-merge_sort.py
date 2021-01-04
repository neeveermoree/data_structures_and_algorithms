def merge_sort(arr):
    length = len(arr)
    if length == 1:
        return arr
    middle = length // 2
    return  merge(merge_sort(arr[:middle]), merge_sort(arr[middle:]))


def merge(arr1, arr2):
    merged_arr = []

    length1 = len(arr1)
    length2 = len(arr2)
    
    i1 = 0
    i2 = 0
    while i1 != length1 or i2 != length2:
        if i1 == length1:
            merged_arr.append(arr2[i2])
            i2 += 1
        elif i2 == length2:
            merged_arr.append(arr1[i1])
            i1 += 1
        else:
            if arr1[i1] <= arr2[i2]:
                merged_arr.append(arr1[i1])
                i1 += 1
            else:
                merged_arr.append(arr2[i2])
                i2 += 1
    return merged_arr


a = [1, 9, -1, -2, 0, 1, 5, 3, 2, 7]
print(merge_sort(a))

                            #                                                 1 9 -1 -2 0 1 5 3 2 7
                            #                                 1a) 1 9 -1 -2 0                      1b) 1 5 3 2 7
                            #                     2a) 1 9 -1             2b) -2 0        2c) 1 5 3          2d) 2 7
                            #         3a) 1 9          3b) -1       3c) -2      3d) 0   3e) 15   3f) 3   3g) 2    3h) 7
                            # 4a) 1        4b) 9                                   4c) 1     4d) 5             

                            #         1 9                                                  15
                            #                 -1 1 9                       -2 0                 1 3 5          2 7
                            #                                 -2 -1 0 1 9                             1 2 3 5 7
                            #                                                 -2 -1 0 1 1 2 3 5 7 9
