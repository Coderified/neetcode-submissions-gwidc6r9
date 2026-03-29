# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        q=deque()
        q.append(root)
        l=[]

        while q:
            lvl = len(q)
            
            for _ in range(lvl):
                val = q.popleft()
                l.append(val.val)
                if val.left:
                    q.append(val.left)
                if val.right:
                    q.append(val.right)
        
        l.sort()
        print(l)
        return l[k-1]
            
                
        