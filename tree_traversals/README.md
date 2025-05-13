# Tree Traversal Algorithms 🌳

**Tree Traversal** refers to the process of visiting (checking and/or updating) each node in a tree data structure, exactly once, in a systematic way.

---

## 📌 Types of Tree Traversals

There are two main categories:

### 1. **Depth-First Traversal (DFS)**

- **Inorder (Left, Root, Right)**
- **Preorder (Root, Left, Right)**
- **Postorder (Left, Right, Root)**

### 2. **Breadth-First Traversal (BFS)**

- Also known as **Level Order Traversal**

---

## 🌲 Example Binary Tree

```
        A
       / \
      B   C
     /   / \
    D   E   F
```

---

## 🧠 Use Cases

- **Inorder**: Get values in sorted order (for BSTs)
- **Preorder**: Used to copy/serialize trees
- **Postorder**: Useful for deleting/freeing trees
- **Level Order**: Shortest path, used in BFS problems

---

## ⏱️ Time & Space Complexity

| Traversal      | Time Complexity | Space Complexity |
|----------------|------------------|------------------|
| Inorder        | O(n)             | O(h)             |
| Preorder       | O(n)             | O(h)             |
| Postorder      | O(n)             | O(h)             |
| Level Order    | O(n)             | O(w)             |

- `n`: total nodes
- `h`: height of the tree
- `w`: maximum width of the tree

---

## 📈 Visualization

![gif](https://upload.wikimedia.org/wikipedia/commons/4/48/Inorder-traversal.gif)
![gif](https://upload.wikimedia.org/wikipedia/commons/a/ac/Preorder-traversal.gif)
![gif](https://upload.wikimedia.org/wikipedia/commons/2/28/Postorder-traversal.gif)

---

## 🖼️ Resources

- Tree visualizer tools
- Step-by-step animations
- Online tree drawing editors

---

## 📚 Related Topics

- Binary Search Trees (BST)
- Recursion
- Queues and Stacks

