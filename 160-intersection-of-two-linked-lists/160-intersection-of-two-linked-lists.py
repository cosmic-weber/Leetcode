# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        section = set()
        while headA != None:
            section.add(id(headA))
            headA = headA.next
        
        while headB != None:
            if id(headB) in section:
                return headB
            headB = headB.next
        return None