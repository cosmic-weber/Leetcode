# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        childs = set()
        dct = {}
        for lst in descriptions:
            node = dct.setdefault(lst[0], TreeNode(lst[0]))
            child = dct.setdefault(lst[1], TreeNode(lst[1]))
            if lst[2] == 1:
                node.left = child
            else:
                node.right = child
            childs.add(lst[1])
        
        for lst in descriptions:
            if lst[0] not in childs:
                return dct[lst[0]]