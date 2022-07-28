# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if root:
            self.flatten(root.right)
            self.flatten(root.left)
            root.left = None
            root.right = self.prev
            self.prev = root
            
            
            # temp = root.right
            # while root.right:
            #     root = root.right
            # root.right = temp
#         def traverse(node):
#             if not node:
#                 return None
#             if node.left:
#                 n = node.left
                
#                 while n.right:
#                     n = n.right
#                 n.right = node.right
#                 node.right = node.left
#                 node.left = None
#             traverse(node.right)
#         traverse(root)
        