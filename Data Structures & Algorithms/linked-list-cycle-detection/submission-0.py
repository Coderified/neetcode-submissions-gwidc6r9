# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l=[head.val]

        while head.next:
            head=head.next
            l.append(head.val)
            print(head.val)
            if head.next and head.next.val in l:
                return True
        return False
        