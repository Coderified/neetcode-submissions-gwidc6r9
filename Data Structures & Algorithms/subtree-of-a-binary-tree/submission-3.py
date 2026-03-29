# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if subRoot is None:
            return True
        if root is None:
            return False
        def sametreecheck(root,subRoot):
            if root is None and subRoot is None:
                return True
            if root is None and subRoot is not None:
                return False
            if root and subRoot and root.val==subRoot.val:
                return ((root.val==subRoot.val) and 
                    sametreecheck(root.left,subRoot.left) and 
                    sametreecheck(root.right,subRoot.right) )
            return False
        if sametreecheck(root,subRoot):
            return True
        
        return (self.isSubtree(root.left,subRoot) or
                self.isSubtree(root.right,subRoot))

        


        


        