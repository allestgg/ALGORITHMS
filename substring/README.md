# Substring Search Algorithm 🔎

This is a basic implementation of a **Substring Search** algorithm that finds all starting indices where a given substring appears in a main string.

---

## 📌 How It Works

The algorithm slides the substring over the main string and compares character by character.  
If all characters match at a given position, it saves the starting index of the match.

> Example:  
Main string: `"abracadabra"`  
Substring: `"abra"`  
Result: `[0, 7]` (positions where the substring is found)

---

## 🧠 Explanation

- `n - m + 1` defines the last possible index where the substring can fit.
- The loop checks every index `i` to see if the substring matches from that point onward.
- If all characters match, the starting index `i` is added to the result list.

---

## 🔍 Time Complexity

- **Best Case:** `O(n)` (if substring found early)
- **Worst Case:** `O(n * m)`  
  (n = length of string, m = length of substring)

---

## ✅ Pros

- Easy to understand and implement
- Works with any string
- Returns all occurrences, not just the first

---

## ❌ Cons

- Not optimized for long texts or many searches
- Slower than advanced algorithms like KMP or Boyer-Moore

---

## 🧩 Use Cases

- Text editors (find & highlight functionality)
- Search engines
- DNA sequence matching