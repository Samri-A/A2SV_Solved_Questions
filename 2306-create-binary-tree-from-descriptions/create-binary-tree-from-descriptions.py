# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        tree = {}
        childs = set()

        

        for parent  ,  child , isleft in descriptions:

            if parent not in tree:
                tree[parent] = [None] * 2

            if isleft:
                tree[parent][0] = child
            else:
                tree[parent][1] = child

            childs.add(child)

        root = 0

        for parent  ,  child , isleft in descriptions:
            if parent not in childs:
                root = parent
                break

        # print(tree , root)

        


        def constract(root):
            if root is None:
                return 

            

            binary_tree = TreeNode(root)
            if root in tree:
                left , right = tree[root]
                binary_tree.left = constract(left) 
                binary_tree.right = constract(right)

            return binary_tree

             

        return constract(root) 

