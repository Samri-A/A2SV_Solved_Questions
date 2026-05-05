# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def count_left(node):

            h = 0

            while node:
                node = node.left
                h+= 1

            return h

        
        def count_right(node):

            h = 0


            while node:
                node = node.right
                h+= 1

            return h

        h_right = count_right(root)
        h_left = count_left(root)


        if h_left == h_right:
            return (2 ** h_right) - 1

        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)