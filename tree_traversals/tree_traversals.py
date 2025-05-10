class Node:
    def __init__(self, value):
        self.value  = value
        self.left   = None
        self.right  = None

def inorder_traversal(node: Node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.value)
        inorder_traversal(node.right)

def preorder_traversal(node: Node):
    if node is not None:
        print(node.value)
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def postorder_traversal(node: Node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value)


# Crear un árbol binario de ejemplo
#
#         A
#        / \
#       B   C
#      / \   \
#     D   E   F

root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('F')

# Probar los recorridos
print("Inorder traversal:")
inorder_traversal(root)  # D B E A C F
print("\nPreorder traversal:")
preorder_traversal(root)  # A B D E C F
print("\nPostorder traversal:")
postorder_traversal(root)  # D E B F C A