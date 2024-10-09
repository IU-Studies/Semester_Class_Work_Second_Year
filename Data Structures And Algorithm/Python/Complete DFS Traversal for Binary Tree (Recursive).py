# Here in this program we will perform Preorder, Inorder, and Postorder Traversal all at once.

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

def preorder(root):
    if root is None:
        return
    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val, end=" ")

root = build_tree()

print("Preorder Traversal is:", end=" ")
preorder(root)
print()

print("Inorder Traversal is:", end=" ")
inorder(root)
print()

print("Postorder Traversal is:", end=" ")
postorder(root)
print()
