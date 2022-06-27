# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        A = ListNode(0)
        head1 = l1
        head2 = l2
        new_head = A
        while True:
            if head1 is None:
                new_head.next = head2
                break
            if head2 is None:
                new_head.next = head1
                break
            if head1.val <= head2.val:
                new_head.next = head1
                head1 = head1.next
            else:
                new_head.next = head2
                head2 = head2.next
                
            new_head = new_head.next
        return A.next