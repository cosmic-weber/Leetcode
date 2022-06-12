# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        return self.arr(root, lst)
        
    def arr(self, root, lst):

        if root != None:
            self.arr(root.left,lst)
            lst.append(root.val)
            self.arr(root.right,lst)
            
        return lst