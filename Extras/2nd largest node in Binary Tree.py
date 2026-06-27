class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.right = Node(4)
root.right.left = Node(2)

def Second_max(root):
    if root is None or (root.left is None and root.right is None):
        return None
    
    child = root
    parent = None

    while child.right is not None:
        parent = child
        child = child.right

    if child.left is not None:
        child = child.left
        while child.left is not None:
            child = child.right
        return child.data

    if parent is not None:
        return parent.data
    
    else:
        return None

print(Second_max(root))



            
