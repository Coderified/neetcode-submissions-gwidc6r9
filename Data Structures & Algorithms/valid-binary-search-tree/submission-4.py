# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def nodecheck(node,mins,maxs):
            if not node:
                return True
            
            if node.val >= maxs or node.val <= mins:
                return False

            return nodecheck(node.left,mins,node.val) and nodecheck(node.right,node.val,maxs) 
        mins = -1*math.inf
        maxs = 1*math.inf
        return nodecheck(root,mins,maxs)
        