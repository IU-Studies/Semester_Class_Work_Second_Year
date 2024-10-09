# In this program we will perform preorder traversal on binary tree (non-recursively) using a stack

class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def build_tree():
    data = int(input("Enter data: "))
    
    if data == -1:
        return None
    
    root = Node(data)
    
    print(f"Enter data in left of {data}")
    root.left = build_tree()
    
    print(f"Enter data in right of {data}")
    root.right = build_tree()
    
    return root

def preorder_non_recursive(root):
    if root is None:
        return
    
    stack = []
    stack.append(root)
    
    while stack:
        node = stack.pop()
        print(node.val, end=" ")
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

root = build_tree()
print("Preorder Traversal (Non-Recursive):", end=" ")
preorder_non_recursive(root)
print()
