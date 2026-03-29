# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev,curr=None,head

        while curr: # go till the curr node exists

        # store next in temp - > then point curr to prev, update prev to vurr 
        # then update curr to temp - > proceed till the last curr i reached
        # there temp is null, so curr is also null prev is the reversed head
        
            temp = curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev

        
        