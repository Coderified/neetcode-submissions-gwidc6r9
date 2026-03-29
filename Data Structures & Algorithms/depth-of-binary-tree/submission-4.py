# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        d=0
        if not root:
            return d
        
        q=deque()
        q.append(root)

        while q:
            for i in range(len(q)):
                x=q.popleft()
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            d+=1
        return d

        