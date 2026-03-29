# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        
        q=deque()
        q.append(root)
        l=[]
        if root is None:
            return l
        while q:
            lens = len(q)
            l1=[]
            for i in range(lens):
                vals = q.popleft()
                l1.append(vals.val)
                if vals.left:
                    q.append(vals.left)
                if vals.right:
                    q.append(vals.right)
            l.append(l1)
        return l
                
                
        