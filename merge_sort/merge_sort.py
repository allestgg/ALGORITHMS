def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])    # Starts in 0 to mid
    right = merge_sort(arr[mid:])   # Starts in mid to final
    return merge(left, right)

arr = [3, 7, 2, 9, 1, 6, 8, 5, 4]
sorted_arr = merge_sort(arr)
print(f"Original array: {arr}")
print(f"Ordered arrey: {sorted_arr}")

'''
                                [3, 7, 2, 9, 1, 6, 8, 5, 4]
                                      /               \
                        [3, 7, 2, 9]                    [1, 6, 8, 5, 4]
                          /      \                         /         \
                  [3, 7]         [2, 9]             [1, 6]         [8, 5, 4]
                   / \            /  \               / \            /     \
                [3] [7]        [2]  [9]           [1] [6]      [8]     [5, 4]
                                                                                 /   \
                                                                              [5]   [4]
'''

'''
                                [1, 2, 3, 4, 5, 6, 7, 8, 9]
                                      /               \
                        [2, 3, 7, 9]                    [1, 4, 5, 6, 8]
                          /      \                         /         \
                  [3, 7]         [2, 9]             [1, 6]         [4, 5, 8]
                   / \            /  \               / \            /     \
                [3] [7]        [2]  [9]           [1] [6]      [8]     [4, 5]
                                                                                 /   \
                                                                              [5]   [4]

'''