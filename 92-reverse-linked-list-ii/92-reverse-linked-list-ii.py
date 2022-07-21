# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        if len(lst) == 1:
            return ListNode(lst[0])
        left-=1
        right-=1
        lts = lst[left:right+1]
        lst = lst[:left]+lts[::-1]+lst[right+1:]
        return self.ll(lst)
        
    def ll(self, lst):
        head = ListNode(lst[0])
        cur = head
        for i in range(1,len(lst)):
            cur.next = ListNode(lst[i])
            cur = cur.next
        return head