# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parents = {root: None}
        
        while p not in parents or q not in parents:
            node = stack.pop()
            if node.left:
                parents[node.left] = node
                stack.append(node.left)
            if node.right:
                parents[node.right] = node
                stack.append(node.right)
        ans = set()    
        while p:
            ans.add(p)
            p = parents[p]
            
        while q not in ans:
            q = parents[q]
        
        return q