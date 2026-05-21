# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder -   parent left right
        # inorder - left parent right



        index_map = {val: i for i , val in enumerate(inorder)}

        self.pointer = 0

        def build(left , right):

            if left > right:
                return None
            
            root_val = preorder[self.pointer]

            self.pointer+=1



            root = TreeNode(root_val)

            mid = index_map[root_val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1 , right )

            return root

        

        
        # print(index_map)

        return build(0 , len(inorder)-1)


        
