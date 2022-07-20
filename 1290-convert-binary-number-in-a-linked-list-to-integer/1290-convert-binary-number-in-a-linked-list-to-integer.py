# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        lst = []
        s = ''
        while head:
            lst.append(head.val)
            head = head.next
        for i in lst:
            s+=str(i)
        decimal,i = 0,0
        for c in s[::-1]:
            decimal += pow(2,i) * int(c)
            i += 1
        return decimal