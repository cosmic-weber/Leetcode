"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        lst = []
        self.recursive(root, lst)
        return lst
        
    def recursive(self, root, lst):
        if root is None:
            return 
        lst.append(root.val)
        if root.children:
            for child in root.children:
                self.recursive(child, lst)
                