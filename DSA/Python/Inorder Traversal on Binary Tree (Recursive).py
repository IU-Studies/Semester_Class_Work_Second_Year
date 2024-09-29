# In this program we will perform Inorder traversal on a binary tree

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

def inorder(root):
    if root is None:
        return
    
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

root = build_tree()
print("Inorder Traversal:", end=" ")
inorder(root)
