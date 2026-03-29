# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if not p and not q:
        #     return True
        # if (p and not q) or (q and not p):
            
        #     return False
        
    
        # if p.val!=q.val:
        #     return False
        # # else:
        # #     return (self.isSameTree(p.left,q.left) and
        #     self.isSameTree(p.right,q.right))
        
        p1=deque([p])
        q1=deque([q])

        while p1 and q1:
            
            for _ in range(len(p1)):

                nodep = p1.popleft()
                nodeq = q1.popleft()

                if not nodep and not nodeq:
                    continue
                if (nodep and not nodeq) or (nodeq and not nodep):
                    return False
                if nodep.val!=nodeq.val:
                    return False
                
                p1.append(nodep.left)
                
                p1.append(nodep.right)

                q1.append(nodeq.left)
                
                q1.append(nodeq.right)

        return True

            


        