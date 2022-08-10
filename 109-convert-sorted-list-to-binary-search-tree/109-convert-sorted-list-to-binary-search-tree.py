# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        print(lst)
        return self.tree(lst)
        
    def tree(self, lst):
        if not lst:
            return None
        mid = len(lst)//2
        root = TreeNode(lst[mid])
        root.left = self.tree(lst[:mid])
        root.right = self.tree(lst[mid+1:])
        return root