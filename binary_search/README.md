# Binary Search 📚

Binary Search is an efficient algorithm for finding an element in a **sorted** list. It works by repeatedly dividing the search interval in half.

> Time Complexity: **O(log n)**  
> Space Complexity: **O(1)** (iterative), **O(log n)** (recursive)

---

## 🔍 How It Works

1. Start with the full range: `low = 0`, `high = length - 1`
2. Find the middle: `mid = (low + high) // 2`
3. Compare the target with `array[mid]`:
   - If equal → 🎯 Element found
   - If less → Search left half (`high = mid - 1`)
   - If greater → Search right half (`low = mid + 1`)
4. Repeat until found or `low > high`

---

## 📌 Requirements

- The array **must be sorted** in ascending order.
- Works on both numbers and strings.

---

## 📈 Visualization

![gif](https://d18l82el6cdm1i.cloudfront.net/uploads/bePceUMnSG-binary_search_gif.gif)

---

## ✅ Pros

- Much faster than linear search on large datasets.
- Minimal memory usage (in iterative form).

---

## ⚠️ Cons

- Requires sorted data.
- More complex than linear search.

