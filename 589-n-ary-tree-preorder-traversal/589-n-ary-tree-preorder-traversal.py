"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        lst = []
        self.ll(root, lst)
        return lst
        
    def ll(self, root, lst):
        s = []
        s.append(root)
        while s:
            node = s.pop()
            lst.append(node.val)
            if node.children:
                s += node.children[::-1]

# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         lst = []
#         self.recursive(root, lst)
#         return lst
        
#     def recursive(self, root, lst):
#         if root is None:
#             return 
#         lst.append(root.val)
#         if root.children:
#             for child in root.children:
#                 self.recursive(child, lst)
                