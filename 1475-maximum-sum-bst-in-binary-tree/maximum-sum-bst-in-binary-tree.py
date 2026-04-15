# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        maximum_sum = [0]
        
        def track_sum(node):


            if not node:
                return ( 0 ,   True,    float('-inf') , float('inf') )

            left_sum ,  left_isBST   , left_maxLeft , leftminLeft = track_sum(node.left)
            right_sum , right_isBST ,  right_maxRight ,  right_minRight = track_sum(node.right)
            
            if left_isBST and right_isBST and left_maxLeft < node.val < right_minRight:
                    maximum_sum[0] = max( left_sum + node.val + right_sum ,maximum_sum[0] )
                    return (  left_sum + node.val + right_sum ,  True,   max(right_maxRight , node.val) ,  min(leftminLeft , node.val) )
            

            
            return ( 0 ,  False,  0 , 0 )

             
        
        vals = track_sum(root)

        return maximum_sum[0]



