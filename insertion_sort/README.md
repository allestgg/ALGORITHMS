# Insertion Sort Algorithm 🧩

**Insertion Sort** is a simple comparison-based sorting algorithm that builds the final sorted array one item at a time.

---

## 📌 How It Works

It iterates through the array and, at each iteration, removes one element from the input data, finds the location it belongs within the sorted part, and inserts it there.

> Example:  
Unsorted: `[5, 2, 4, 6, 1, 3]`  
Sorted:   `[1, 2, 3, 4, 5, 6]`

---

## 💻 Python Implementation

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
```

---

## 🔍 Time Complexity

- **Best Case:** `O(n)` (Already sorted)
- **Average Case:** `O(n^2)`
- **Worst Case:** `O(n^2)` (Reversed array)
- **Space Complexity:** `O(1)` (In-place)

---

## ✅ Pros

- Simple to implement
- Efficient for small datasets
- In-place algorithm (no extra space)

---

## ❌ Cons

- Inefficient on large lists
- Not suitable for real-time systems with large datasets

---

## 📈 Visualization

![gif](https://swtestacademy.com/wp-content/uploads/2021/11/insertion-sort.gif)

---

## 📚 Real-World Use

- Often used in teaching and learning sorting concepts
- Used in hybrid sorting algorithms (like TimSort)
