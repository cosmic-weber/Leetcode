# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        self.traversal(root, lst)
        return lst
    
    def traversal(self, root, lst):
        if root:
            lst.append(root.val)
            self.traversal(root.left, lst)
            self.traversal(root.right, lst)
            