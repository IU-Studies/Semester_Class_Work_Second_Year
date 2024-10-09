# In this program we will perform Preorder traversal on a binary tree

class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def build_tree():
    data = int(input("Enter data : "))
    
    if data == -1:
        return None
    
    root = Node(data)
    
    print(f"Enter data in left of {data}:")
    root.left = build_tree()
    
    print(f"Enter data in right of {data}:")
    root.right = build_tree()
    
    return root

def preorder(root):
    if root is None:
        return
    
    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)

root = build_tree()
print("Preorder Traversal:")
preorder(root)
