# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Rev second half

        prev=None
        curr=slow
        while curr:
            tmp=curr.next
            curr.next=prev
            prev=curr
            curr=tmp

        new=head
        reverse=prev

        while reverse.next:
            tmp1=new.next
            tmp2=reverse.next
            new.next = reverse
            reverse.next=tmp1
            new=tmp1
            reverse=tmp2

        print(head)


        