# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        self.count = 0

        prefix = defaultdict(int) 
        prefix[0] = 1

        def dfs(node , sum_):  

            if node is None:
                return 


            sum_ += node.val

            self.count += prefix[ sum_ - targetSum]
 
            prefix[sum_] += 1
            
            dfs(node.left , sum_)
            dfs(node.right , sum_)

            prefix[sum_] -= 1

            

        dfs(root , 0)

        return self.count

        