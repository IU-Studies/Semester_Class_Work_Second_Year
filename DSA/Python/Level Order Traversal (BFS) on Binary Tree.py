# In this program we will perform level order traversal or breadth-first search (BFS) traversal on a binary tree

from collections import deque

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

def level_order_traversal(root):
    if root is None:
        return
    
    queue = deque([root])
    
    while queue:
        temp = queue.popleft()
        print(temp.val, end=" ")
        
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)

root = build_tree()
print("Level Order Traversal:", end=" ")
level_order_traversal(root)
print()
