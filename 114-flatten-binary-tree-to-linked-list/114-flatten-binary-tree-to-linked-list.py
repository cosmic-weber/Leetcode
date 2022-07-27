# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def traverse(node):
            if not node:
                return None
            if node.left:
                n = node.left
                
                while n.right:
                    n = n.right
                n.right = node.right
                node.right = node.left
                node.left = None
            traverse(node.right)
        traverse(root)
        
#         def dfs(root):
        
#             if not root:
#                 return None
            
#             dfs(root.right)
#             dfs(root.left)
            
#             root.right, root.left, self.prev = self.prev, None, root
#             return root
        
#         self.prev = None
#         dfs(root)