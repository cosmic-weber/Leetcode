# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        lst, lst1 = [], []
        lst = self.levelTraversal(p, lst)
        lst1 = self.levelTraversal(q, lst1)
        
        return lst == lst1
        
    def levelTraversal(self, m: Optional[TreeNode], lst) -> list:
        
        if m != None:
            lst.append(m.val)
            self.levelTraversal(m.left, lst)
            self.levelTraversal(m.right, lst)
        else:
            lst.append(0)
        return lst