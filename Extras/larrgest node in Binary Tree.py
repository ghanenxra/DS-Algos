class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.right.right = Tree(4)
# root.right.right.right = Tree(89)



def largest_no(root):
    if root is None:
        return -1
    
    while root.right is not None:
        root = root.right
    return root.data

print(largest_no(root))