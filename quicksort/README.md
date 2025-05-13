# Quicksort Algorithm ⚡

**Quicksort** is a highly efficient and widely used sorting algorithm based on the **divide-and-conquer** approach.

---

## 🧠 How It Works

1. Choose a **pivot** element from the array.
2. Partition the array into two sub-arrays:
   - Elements less than the pivot
   - Elements greater than the pivot
3. Recursively apply the same process to the sub-arrays.

---

## 🔢 Example

```
Original: [10, 7, 8, 9, 1, 5]
→ [1, 7, 8, 9, 10, 5] 
→ [1, 5, 8, 9, 10, 7] 
→ [1, 5, 7, 9, 10, 8] 
→ [1, 5, 7, 8, 10, 9] 
→ [1, 5, 7, 8, 9, 10]

```
---

## 📈 Time & Space Complexity

| Case       | Time Complexity | Space Complexity |
|------------|------------------|------------------|
| Best       | O(n log n)       | O(log n)         |
| Average    | O(n log n)       | O(log n)         |
| Worst      | O(n²)            | O(log n)         |

- `n`: number of elements in the array

---

## ✅ Pros

- Very fast in practice
- In-place version exists (less memory usage)
- Works well for large datasets

---

## ❌ Cons

- Worst-case time complexity is O(n²)
- Not stable (doesn't preserve the order of equal elements)

---

## 📌 When to Use

- When average-case performance is more important than guaranteed worst-case
- When memory usage is a concern (using in-place version)

---

## 📊 Visualization

![gif](https://www.lavivienpost.net/wp-content/uploads/2022/02/quicksort-600-1.gif)
