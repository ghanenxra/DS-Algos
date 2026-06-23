class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(4)
root.left = Node(8)
root.right = Node(12)
root.left.left = Node(16)
root.right.left = Node(20   )

def Height(root):
    if root is None:
        return -1

    if root:
        left_height = Height(root.left)
        right_height = Height(root.right)
        return 1 + max(left_height,right_height)

def CheckLeftorRight(root, value):
    if root is None:
        return
    
    if root.data == value:
        return "Node found in Root"

    if CheckLeftorRight(root.left, value):
        return "Root found in left Subtree"
    
    if CheckLeftorRight(root.right, value):
        return "Node found in Right Subtree"

def CheckNode(root, value):
    if root is None:
        return False
    
    if root.data == value:
        return True

    return CheckNode(root.left, value) or CheckNode(root.right, value)

count = 0
def TreeCount(root):
    global count
    if root is not None:
        TreeCount(root.left)
        count += 1
        TreeCount(root.right)
    return count

def TreePrint(root):
    if root is not None:
        "Inorder Traversal"
        TreePrint(root.left)
        print(root.data)
        TreePrint(root.right)

        "Pre-Order Traversal"
        print(root.data)
        TreePrint(root.left)
        TreePrint(root.right)

        "Post-Order Traversal"
        TreePrint(root.left)
        TreePrint(root.right)
        print(root.data)

        return root

TreePrint(root)
print("Number of nodes in the tree: ", TreeCount(root))
print("Does node with value 5 exist ? ", CheckNode(root,5))
print(CheckLeftorRight(root,2))
print("Height of Tree", Height(root))


    






