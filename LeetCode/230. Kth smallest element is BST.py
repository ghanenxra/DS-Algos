# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_storage = []

        def Inorder(root):
            if root is None:
                return None
            
            Inorder(root.left)
            sorted_storage.append(root.val)
            Inorder(root.right)

        Inorder(root)

        return sorted_storage[k-1]