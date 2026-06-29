class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(500)

# ── Level 1 ───────────────────────────────────────────
root.left  = TreeNode(250)
root.right = TreeNode(750)

# ── Level 2 ───────────────────────────────────────────
root.left.left   = TreeNode(125)
root.left.right  = TreeNode(375)
root.right.left  = TreeNode(625)
root.right.right = TreeNode(875)

# ── Level 3 ───────────────────────────────────────────
root.left.left.left    = TreeNode(62)
root.left.left.right   = TreeNode(187)
root.left.right.left   = TreeNode(312)
root.left.right.right  = TreeNode(437)
root.right.left.left   = TreeNode(562)
root.right.left.right  = TreeNode(687)
root.right.right.left  = TreeNode(812)
root.right.right.right = TreeNode(937)

# ── Level 4 ───────────────────────────────────────────
root.left.left.left.left    = TreeNode(31)   
root.left.left.left.right   = TreeNode(93)    
root.right.left.left.right  = TreeNode(593)  
root.right.right.left.right = TreeNode(843)   

# ── Level 5 ───────────────────────────────────────────
root.left.left.left.left.left     = TreeNode(15)   
root.right.left.left.right.left   = TreeNode(580)  
root.right.right.left.right.left  = TreeNode(836)  

# ── Level 6 ───────────────────────────────────────────
root.left.left.left.left.left.left     = TreeNode(7)   
root.right.left.left.right.left.left   = TreeNode(575) 
root.right.right.left.right.left.left  = TreeNode(830)  

# ── Level 7 ───────────────────────────────────────────
root.left.left.left.left.left.left.left     = TreeNode(3)    
root.right.left.left.right.left.left.left   = TreeNode(572)  
root.right.right.left.right.left.left.left  = TreeNode(828)  

# ── Level 8 ───────────────────────────────────────────
root.left.left.left.left.left.left.left.left     = TreeNode(1)
root.right.left.left.right.left.left.left.left   = TreeNode(570)   
root.right.right.left.right.left.left.left.left  = TreeNode(827)  

""" This Tree data is scraped not human generated"""



def checkBST(root):
    if root is None:
        return True
    if root.right is None and root.left is None:
        return True
    if root.right is not None and root.val < root.left.val:
        return False
    if root.left is not None and root.right.val > root.val:
        return False

    return checkBST(root.left, min_val, root.val) and checkBST(root.right,root.val , max_val)

print(checkBST(root))
    