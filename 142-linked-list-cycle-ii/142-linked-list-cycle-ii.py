# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next == None:
            return None
        slow, fast = head, head.next
        
        while(fast and fast.next and slow and fast!=slow):
            slow = slow.next
            fast = fast.next.next
        
        if fast == slow:
            while (slow.next != head):
                slow = slow.next
                head = head.next
            return head
        return None
            