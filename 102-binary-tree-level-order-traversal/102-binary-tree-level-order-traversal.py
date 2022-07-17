# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            lst = []            
            def bst(root, d):
                if root is None:
                    return
                q = deque()
                q.append(root)
                while q:
                    if d >= len(lst):
                        lst.append([])
                    node = q.popleft()
                    lst[d].append(node.val)
                    bst(node.left, d+1)
                    bst(node.right, d+1)
            
            bst(root, 0)
            
            return lst