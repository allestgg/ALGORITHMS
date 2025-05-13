# Fibonacci Algorithm 🌀

The **Fibonacci sequence** is a series of numbers where each number is the sum of the two preceding ones. It starts from 0 and 1.

> Sequence: `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...`

---

## 🚀 Use Cases

- Algorithm analysis (e.g., recursion performance)
- Financial modeling
- Biological systems (e.g., population growth)
- Dynamic programming practice

---

## 💻 Recursive Implementation (Python)

```python
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
```

---

## 💻 Iterative Implementation (Python)

```python
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

---

## 💻 Dynamic Programming (Memoization)

```python
def fibonacci_dp(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_dp(n - 1, memo) + fibonacci_dp(n - 2, memo)
    return memo[n]
```

---

## ⚠️ Notes

- Recursive method is simple but **inefficient** for large `n` (exponential time).
- Iterative and DP approaches are much **faster** and **memory-efficient**.

---

## ✅ Pros

- Great for demonstrating recursion and dynamic programming.
- Has mathematical and real-world applications.

---

## ❌ Cons

- Inefficient in its pure recursive form.
- Requires optimization for large values.

