# In this program we will perform inorder traversal on binary tree (non-recursively) using a stack

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

def inorder_non_recursive(root):
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        print(current.val, end=" ") 
        
        current = current.right

root = build_tree()
print("Inorder Traversal (Non-Recursive):", end=" ")
inorder_non_recursive(root)
print()
