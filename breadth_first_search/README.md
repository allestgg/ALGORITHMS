# Breadth-First Search (BFS) 🌐

Breadth-First Search (BFS) is an algorithm for traversing or searching **graph** or **tree** data structures. It explores all the neighbor nodes at the current depth before moving on to the next level.

> Time Complexity: **O(V + E)**  
> Space Complexity: **O(V)**  
> Where `V` = number of vertices, `E` = number of edges

---

## 🚀 How It Works

1. Start from the initial node (source).
2. Mark it as visited and add it to a queue.
3. While the queue is not empty:
   - Dequeue a node and process it.
   - Enqueue all **unvisited** neighbors and mark them as visited.
4. Repeat until all reachable nodes are visited.

---

## 📌 Requirements

- Can be used on **graphs** (directed or undirected) or **trees**.
- No need for sorted input.

---

## 📈 Visualization

### DFS VS BFS
![gif](https://miro.medium.com/v2/resize:fit:1280/1*GT9oSo0agIeIj6nTg3jFEA.gif)

---

## ✅ Pros

- Finds the **shortest path** (fewest edges) in unweighted graphs.
- Simple and easy to implement.

---

## ⚠️ Cons

- Requires additional memory (queue + visited set).
- Can be slow in very large graphs if not optimized.
