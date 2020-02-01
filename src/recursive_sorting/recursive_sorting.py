# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []
    # TO-DO
    # curr_max = arrA[0]
    # a = 0  # index a
    # b = 0  # index b

    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] > arrB[0]:
            merged_arr.append(arrB.pop(0))
        else:
            merged_arr.append(arrA.pop(0))

    return merged_arr + arrA + arrB

    # for i in range(0, elements):
    #     if a >= len(arrA):
    #         merged_arr[i] = arrB[b]
    #         b += 1

    #     elif b >= len(arrB):
    #         merged_arr[i] = arrA[a]
    #         a += 1

    #     elif arrB[b] > curr_max:
    #         merged_arr[i] = arrA[a]
    #         a += 1
    #         curr_max = arrB[b]

    #     elif arrA[a] > curr_max:
    #         merged_arr[i] = arrB[b]
    #         b += 1
    #         curr_max = arrA[a]

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr

    ind = len(arr) // 2
    arr_l = arr[:ind]
    arr_r = arr[ind:]

    arr_l = merge_sort(arr_l)
    arr_r = merge_sort(arr_r)

    return merge(arr_l, arr_r)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
