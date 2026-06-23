'''
Definition for Node
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def height(self, root):
        if root is None:
            return -1
            
        elif root: 
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            
            return 1 + max(left_height, right_height)
        