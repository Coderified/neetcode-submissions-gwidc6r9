# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        plist = deque([p])
        qlist = deque([q])

        

        while plist and qlist:
            print("___")
            lvl =len(plist)
            nodep = plist.popleft()
            nodeq = qlist.popleft()

            if not nodep and not nodeq:
                continue
            if (not nodep and nodeq) or (not nodeq and nodep) or (nodep.val!=nodeq.val):
                return False
            
            for i in range(lvl):
                if (not nodep.left and nodeq.left) or (not nodeq.left and nodep.left) or (not nodep.right and nodeq.right) or (not nodeq.right and nodep.right):
                    return False

                if nodep.left: 
                    plist.append(nodep.left)
                if nodeq.left: 
                    qlist.append(nodeq.left)
                if nodep.right:
                    plist.append(nodep.right) 
                if nodeq.right:
                    qlist.append(nodeq.right)
        return True




        


        