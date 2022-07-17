# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lst = []
        def DFS(root):
            if not root:
                return
            else:
                DFS(root.left)
                lst.append(root.val)
                DFS(root.right)
            
        DFS(root)
        larger = lst[0]
        for i in range(1, len(lst)):
            if larger >= lst[i]:
                return False
            larger = lst[i]
        return True