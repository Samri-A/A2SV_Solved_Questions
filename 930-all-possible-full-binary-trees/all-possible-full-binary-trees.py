# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        def explore_FBT(n):

            if n == 1:
                return [TreeNode(0)]
                
            result = []
    
            for left_size in range(1 ,n):
                right_size = n - 1 - left_size

                left = explore_FBT(left_size)
                right = explore_FBT(right_size)

                for left_tree in left:
                    for right_tree in right:
                        root = TreeNode(0)
                        root.left = left_tree
                        root.right = right_tree
                        result.append(root)

                
            return result


        
        return explore_FBT(n)

            

            


            
