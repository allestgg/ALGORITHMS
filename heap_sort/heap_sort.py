def heapify(arr, n, i):
    largest = i 
    left = 2 * i + 1            # 1->5
    right = 2 * i + 2           # 1->6

    if left < n and arr[left] > arr[largest]: #1-> 5<6 and 7>13
        largest = left          # 1-> largest=5
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Needed to send the item changed as leaf
        heapify(arr, n, largest)

def  heap_sort(arr):
    n = len(arr)
    # Building max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)                  # for this example we send arr, 6, i
    # Send the major at the end of the list
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i , 0)

arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print(f"Ordered array: {arr}")