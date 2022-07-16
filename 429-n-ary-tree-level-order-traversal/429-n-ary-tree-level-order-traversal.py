"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        lst = []
        self.ll(root, lst, 0)
        return lst
                
    def ll(self, root, lst, d):
        
        if d >= len(lst):
            lst.append([])
            
        lst[d].append(root.val)
        if root.children:
            for child in root.children:
                self.ll(child, lst, d+1)