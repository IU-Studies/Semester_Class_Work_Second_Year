# In this program we will perform postorder traversal on a binary tree (non-recursively) using a stack

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

def postorder_non_recursive(root):
    if root is None:
        return
    
    stack = []
    last_visited = None
    current = root
    
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        
        peek_node = stack[-1]
        
        if peek_node.right and last_visited != peek_node.right:
            current = peek_node.right
        else:
            print(peek_node.val, end=" ")
            last_visited = stack.pop()

root = build_tree()
print("Postorder Traversal (Non-Recursive):", end=" ")
postorder_non_recursive(root)
print()
