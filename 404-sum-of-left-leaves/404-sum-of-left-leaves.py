# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.suM = 0
        return self.leaf(root, False)
    
    def leaf(self, root, left):
        if not root:
            return 0
        if left and root.left is None and root.right is None:
            self.suM += root.val
        self.leaf(root.left, True)
        self.leaf(root.right, False)
        
        return self.suM
                