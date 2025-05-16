# Merge Sort Algorithm 🧩

**Merge Sort** is a stable, efficient, comparison-based sorting algorithm based on the **divide-and-conquer** paradigm.

---

## 🧠 How It Works

1. Divide the array into two halves.
2. Recursively sort both halves.
3. Merge the two sorted halves into a single sorted array.

---

## 🔢 Example

```
Original: [6, 3, 8, 5, 2]
Step 1: Divide → [6, 3], [8, 5, 2]
Step 2: Sort each → [3, 6], [2, 5, 8]
Step 3: Merge → [2, 3, 5, 6, 8]
```

---

## 📈 Time & Space Complexity

| Case       | Time Complexity | Space Complexity |
|------------|------------------|------------------|
| Best       | O(n log n)       | O(n)             |
| Average    | O(n log n)       | O(n)             |
| Worst      | O(n log n)       | O(n)             |

- `n`: number of elements in the array

---

## ✅ Pros

- Always runs in O(n log n)
- Stable sorting algorithm
- Good for large datasets

---

## ❌ Cons

- Not in-place (uses extra memory)
- Slower than Quicksort in practice on small arrays

---

## 📌 When to Use

- When stability is required
- For linked lists (merge sort works especially well on them)

---

## 📊 Visualization

![gif](https://www.lavivienpost.net/wp-content/uploads/2022/02/merge-sort-400.gif)