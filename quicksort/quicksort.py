def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1
    
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

arr = [10, 7, 8, 9, 1, 5] # [1, 7, 8, 9, 10, 5] -> [1, 5, 8, 9, 10, 7] -> [1, 5, 7, 9, 10, 8] -> [1, 5, 7, 8, 9, 10]
n = len(arr)
quicksort(arr, 0, n - 1)
print(f"Array ordered: {arr}")