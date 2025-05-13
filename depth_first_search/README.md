# Depth-First Search (DFS) 🌲

**Depth-First Search (DFS)** is a graph traversal algorithm that explores as far down a branch of the graph as possible before backtracking. It is commonly used for searching, pathfinding, and solving problems like maze traversal.

> Time Complexity: **O(V + E)**  
> Space Complexity: **O(V)**  
> Where `V` = number of vertices, `E` = number of edges

---

## 🚀 How It Works

1. Start at the root node (or any arbitrary node).
2. Visit the current node and mark it as visited.
3. Explore all the neighbors of the current node by moving deeper (recursively or using a stack).
4. If there are no more unvisited neighbors, backtrack to the previous node and repeat until all nodes are visited.

---

## 📌 Requirements

- Can be used on **graphs** (directed or undirected) and **trees**.
- Typically implemented recursively or using a stack.

---

## 📈 Visualization

![gif](https://miro.medium.com/v2/resize:fit:1280/1*GT9oSo0agIeIj6nTg3jFEA.gif)


---

## ✅ Pros

- Simple to implement (especially recursively).
- Good for exploring all possibilities or finding paths in a graph.

---

## ⚠️ Cons

- May use a lot of memory for large graphs due to the recursion stack.
- Not guaranteed to find the shortest path.
