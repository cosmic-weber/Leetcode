# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        lst = []
        self.inorder(root, lst)
        
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if lst[i] + lst[j] == k:
                    return True
        
    def inorder(self, root, lst) -> list:
        
        if root:
            self.inorder(root.left, lst)
            lst.append(root.val)
            self.inorder(root.right, lst)
            
        return lst