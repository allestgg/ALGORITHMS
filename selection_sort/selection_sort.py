def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i 
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


my_list = [34, 632, 45, 11, 1, 0, 98, 22, 4312]
ordered_list = selection_sort(my_list)
print(f'Ordered list: {ordered_list}')