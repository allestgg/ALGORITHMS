def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
    
arr = [1, 3, 5, 7, 9, 11, 13]
target = 5
result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} is on this position: {result + 1}")
else:
    print(f"Target doesn't exist in list")
