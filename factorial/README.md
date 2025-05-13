# Factorial Algorithm ➗

The **Factorial** of a non-negative integer `n` is the product of all positive integers less than or equal to `n`. It is denoted by `n!`.

> Example: `5! = 5 × 4 × 3 × 2 × 1 = 120`

---

## 📌 Definition

`n! = n × (n - 1) × (n - 2) × ... × 1`  
`0! = 1` (by definition)

---

## 🚀 Use Cases

- Combinatorics (e.g., permutations and combinations)
- Probability theory
- Mathematical series (like Taylor series)
- Algorithm analysis

---

## 💻 Recursive Implementation (Python)

```python
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
```

---

## 💻 Iterative Implementation (Python)

```python
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

---

## ⚠️ Constraints

- Input should be a non-negative integer.
- Recursive approach may hit the recursion limit for large `n`.

---

## ✅ Pros

- Simple to implement.
- Useful in many mathematical and computational problems.

---

## ❌ Cons

- Recursive version is not suitable for large inputs due to stack overflow.

---
