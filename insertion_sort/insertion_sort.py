def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]           # Next pos = prev pos
            j -= 1
        arr[j + 1] = key                # Prev pos = next pos
    return arr

arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print(f"Sorted array: {sorted_arr}")