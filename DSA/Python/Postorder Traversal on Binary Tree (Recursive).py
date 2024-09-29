# In this program we will perform Postorder traversal on a binary tree

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

def postorder(root):
    if root is None:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.val, end=" ")

root = build_tree()
print("Postorder Traversal:", end=" ")
postorder(root)
