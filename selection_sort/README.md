# Selection Sort Algorithm 🟡

**Selection Sort** is a simple sorting algorithm that repeatedly selects the smallest (or largest) element from the unsorted portion and moves it to the beginning.

---

## 📌 How It Works

1. Divide the array into a sorted and unsorted part.
2. Repeatedly select the smallest element from the unsorted part.
3. Swap it with the first unsorted element.
4. Continue until the entire array is sorted.

> Example:  
Unsorted: `[29, 10, 14, 37, 13]`  
Sorted:   `[10, 13, 14, 29, 37]`

---

## 🔍 Time Complexity

- **Best Case:** `O(n^2)`
- **Average Case:** `O(n^2)`
- **Worst Case:** `O(n^2)`
- **Space Complexity:** `O(1)` (In-place)

---

## ✅ Pros

- Simple to understand and implement
- Performs well on small datasets
- In-place (no extra space needed)
- Stable if implemented carefully

---

## ❌ Cons

- Inefficient on large datasets
- Not adaptive (doesn’t benefit from partially sorted input)

---

## 📈 Visualization

![gif](https://swtestacademy.com/wp-content/uploads/2021/11/selection-sort-amination.gif)

---

## 📚 Real-World Use

- Useful for teaching basic sorting principles
- Effective for small datasets or arrays that fit in memory

