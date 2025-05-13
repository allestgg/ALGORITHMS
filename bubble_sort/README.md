# Bubble Sort 🔁

**Bubble Sort** is a simple comparison-based sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

> Time Complexity:  
- Best: **O(n)** (already sorted)  
- Average/Worst: **O(n²)**  

> Space Complexity: **O(1)**  
> Sorting Type: **In-place, Stable**

---

## 🧠 How It Works

1. Start at the beginning of the list.
2. Compare each pair of adjacent items.
3. Swap them if they are in the wrong order.
4. Repeat the process until no swaps are needed (the list is sorted).

---

## 📌 Characteristics

- **Stable**: Preserves the order of equal elements.
- **In-place**: Does not use extra memory.
- **Inefficient** on large datasets.

---

## 📈 Visualization

![gif](https://lh4.googleusercontent.com/proxy/RAdGViOBqCBQnjfxYj55yuRi5G8i85SzA94Bdc5CN9ez2t2ixT_TvliL7lXs3kWH-OdGpCh3aewAWR7dvKX3ZQSBmV-V7Fj_A0UCiNMmFHY-Ac-BaGlATeYq0-3Fs5pPZGkiTA)

---

## ✅ Pros

- Very simple to implement.
- Good for small or nearly sorted data.

---

## ⚠️ Cons

- Extremely slow on large datasets.
- Too many unnecessary comparisons.
