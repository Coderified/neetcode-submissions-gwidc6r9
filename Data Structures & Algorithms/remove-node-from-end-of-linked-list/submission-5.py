# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=0
        copy = head
        
        while copy:
            l+=1
            copy=copy.next
        
        
        op = head
        if l- n==0:
            return op.next
        go_till = 1

        while go_till<(l-n):
            op=op.next
            go_till+=1
        tmp=op.next
        op.next=tmp.next

        return head


        
        
        

        return op
        