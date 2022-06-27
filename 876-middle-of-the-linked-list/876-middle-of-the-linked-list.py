# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        curr = head
        while curr != None:
            lst.append(curr.val)
            curr = curr.next
        n = len(lst)
        
        lst = lst[n//2 : ]
        return self.ll(lst)
        
            
    def ll(self, lst):
        head = ListNode(lst[0])
        cur = head
        for i in range(1, len(lst)):
            cur.next = ListNode(lst[i])
            cur = cur.next
        return head
        