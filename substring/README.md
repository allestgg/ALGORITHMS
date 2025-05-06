# 🔍 Substring Search Algorithms

There are three main variants for substring search algorithms, each with different approaches and efficiencies:

## 1. Brute Force Substring Algorithm 💪
The **Brute Force** algorithm compares the substring with every possible position in the main string. It checks each character one by one, and when a mismatch is found, it breaks out and shifts to the next starting position. This approach has a time complexity of **O(n * m)**, where **n** is the length of the main string and **m** is the length of the substring.

### Example:
The algorithm iterates over the main string, comparing the substring at every possible starting index.

## 2. Fast Search Substring Algorithm ⚡
The **Fast Search Substring** algorithm optimizes the brute force approach by using more advanced techniques (like skipping over some comparisons). It is a general term for algorithms that improve upon brute force by considering preprocessing or heuristics to find substrings faster, often achieving better performance in practice compared to brute force.

### Example:
Specific algorithms like **Rabin-Karp** or **Boyer-Moore** fit into this category by applying hash-based or pattern matching heuristics.

## 3. Knuth-Morris-Pratt (KMP) Algorithm 🚀
The **Knuth-Morris-Pratt (KMP)** algorithm improves substring searching by preprocessing the pattern to create a partial match table (also known as the "failure function"), which allows the algorithm to avoid redundant comparisons. This results in a time complexity of **O(n + m)**, making it more efficient than the brute force approach.

### Example:
The KMP algorithm precomputes information about the pattern and uses that to skip unnecessary checks, leading to better performance when searching for substrings.

---

### 📊 Summary:
- **Brute Force 💪**: Simple but inefficient for large strings, time complexity **O(n * m)**.
- **Fast Search ⚡**: Optimized methods like **Rabin-Karp** or **Boyer-Moore** can achieve better performance in practice.
- **KMP 🚀**: Efficient with **O(n + m)** time complexity by using preprocessing to avoid redundant comparisons.
