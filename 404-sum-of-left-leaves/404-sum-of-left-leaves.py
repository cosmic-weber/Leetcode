# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        lst = [[root, False]]
        ans = 0
        
        while lst:
            node, boo = lst.pop()
            if node:
                if boo and node.left is None and node.right is None:
                    ans += node.val
                lst.append([node.left, True])
                lst.append([node.right, False])
            else:
                ans += 0
        
        return ans
#         self.suM = 0
#         return self.leaf(root, False)
    
#     def leaf(self, root, left):
#         if not root:
#             return 0
#         if left and root.left is None and root.right is None:
#             self.suM += root.val
#         self.leaf(root.left, True)
#         self.leaf(root.right, False)
        
#         return self.suM
                