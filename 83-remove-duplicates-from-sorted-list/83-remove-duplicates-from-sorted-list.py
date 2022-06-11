# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        cur = head
        while cur != None:
            lst.append(cur.val)
            cur = cur.next
        lst1 = []
        
        for i in lst:
            if i not in lst1:
                lst1.append(i)
        
        return self.ll(lst1)
         
    
    def ll(self, arr):
    
        if len(arr)==0:
            return None

        head = ListNode(arr[0])
        last = head

        for data in arr[1:]:

            last.next = ListNode(data)
            last = last.next

        return head
            
        
        