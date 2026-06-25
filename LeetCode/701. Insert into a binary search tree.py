# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)
        if root is None:
            return new_node
        current_node = root

        while True:
            if val < current_node.val:
                if current_node.left is None:
                    current_node.left = new_node
                    break
                
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    break
                current_node = current_node.right

        return root






        # if root.val <= val:
        #     while current_node.left != None:
        #         current_node = current_node.left
        #     if current_node.val >= val:
        #         if current_node.left is None:
        #             current.left = new_node
        #         else:
        #             current.right = new_node
        #     else: 
        #         if current_node.right is None:
        #             current_node.right = new_node

        # if root.val >= val:           

        #     while current_node.right != None:
        #         current_node = current_node.right
        #     if current_node.val>=val:
        #         current_node.left = new_node
        #     else:
        #         current_node.right = new_node


        # return root
            