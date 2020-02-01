# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1-i):
            # print("i = ", i, "j = ", j,"\narr: ", arr)
            if arr[j+1] < arr[j]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

# print("\n\nSORTED: ", bubble_sort([2, 3, 5, 4, 1, 6, 0]))


# # STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    for i in range(0, len(arr)):
        if arr[i] < 0:
            return "Error, negative numbers not allowed in Count Sort"

        elif arr[i] > maximum:
            maximum = arr[i]

    temp = [0] * (maximum + 1)

    for j in range(0, len(arr)):
        temp[arr[j]] += 1

    curr_index = 0

    for k in range(0, maximum+1):
        while temp[k] != 0:
            arr[curr_index] = k
            curr_index += 1
            temp[k] -= 1

    return arr
