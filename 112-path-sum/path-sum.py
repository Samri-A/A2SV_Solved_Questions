# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def helper(root , currentsum):
            if not root:
                return False
                
            currentsum += root.val

            if not root.right and not root.left:
                return targetSum == currentsum

            return helper(root.right , currentsum) or helper(root.left , currentsum)
            
        return helper(root , currentsum = 0)