# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if not root:
            return res
        q=deque()
        q.append(root)
        
        while q:
            l=[]
            for i in range(len(q)):
                
                x=q.popleft()
                l.append(x.val)

                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)

            res.append(l)
        
        return res
