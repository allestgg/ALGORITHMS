# Sequential Search Algorithm 🔍

**Sequential Search** (or **Linear Search**) is the simplest search algorithm that checks each element in a list one by one until it finds the target value or reaches the end.

---

## 📌 How It Works

1. Start at the beginning of the array.
2. Compare each element with the target.
3. If the element matches, return its index.
4. If the end is reached and no match is found, return `-1`.

> Example:  
Searching for `3` in `[7, 2, 5, 3, 9]`  
Result: Found at index `3`

---

## 🔍 Time Complexity

- **Best Case:** `O(1)` (first element is the match)
- **Average Case:** `O(n)`
- **Worst Case:** `O(n)` (target not found or last element)
- **Space Complexity:** `O(1)`

---

## ✅ Pros

- Very simple and easy to implement
- Works on **unsorted** data
- No extra memory needed

---

## ❌ Cons

- Inefficient for large datasets
- Slow compared to binary search on sorted data

---

## 🧪 Test Case

```python
arr = [10, 20, 30, 40, 50]
print(sequential_search(arr, 30))  # Output: 2
print(sequential_search(arr, 60))  # Output: -1
```

---

## 📈 Visualization

![gif](https://www.crio.do/blog/content/images/2022/08/Sequential-Search.gif)

---

## 📚 Real-World Use

- Simple searches in small datasets
- Useful when data is unsorted
- Quick prototyping or teaching purposes

