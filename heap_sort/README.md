# Heap Sort Algorithm ⛏️

**Heap Sort** is a comparison-based sorting technique that uses a **binary heap** data structure to sort elements in-place.

---

## 🧠 How It Works

1. Build a **max heap** from the input array.
2. Swap the root (maximum value) with the last element.
3. Reduce the heap size and heapify the root.
4. Repeat until the array is sorted.

---

## 🔢 Example

```
Original: [4, 10, 3, 5, 1]
Max Heap: [10, 5, 3, 4, 1]
Step-by-step extract max and heapify:
Sorted: [1, 3, 4, 5, 10]
```
---

## 📈 Time & Space Complexity

| Case       | Time Complexity | Space Complexity |
|------------|------------------|------------------|
| Best       | O(n log n)       | O(1)             |
| Average    | O(n log n)       | O(1)             |
| Worst      | O(n log n)       | O(1)             |

- `n`: number of elements in the array

---

## ✅ Pros

- In-place algorithm (no extra memory)
- Consistent O(n log n) performance

---

## ❌ Cons

- Not stable (order of equal elements not preserved)
- More complex to implement than other algorithms

---

## 📌 When to Use

- When memory usage must be minimized
- When consistent performance is preferred over stability

---

## 📊 Visualization

![gif](https://upload.wikimedia.org/wikipedia/commons/f/fe/Heap_sort_example.gif)
