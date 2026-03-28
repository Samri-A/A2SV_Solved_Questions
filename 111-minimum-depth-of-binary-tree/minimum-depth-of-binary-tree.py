# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        left_depth = float('inf') 
        right_depth = float('inf')
            
        if root.left:
            left_depth = 1 + self.minDepth(root.left)
            
        if root.right:
            right_depth = 1 + self.minDepth(root.right)

        return min(left_depth, right_depth )
        
