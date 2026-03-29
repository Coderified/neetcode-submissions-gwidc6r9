# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        def htcheck(root):
            
            if root is None:
                return 0

            leftht = htcheck(root.left)
            if leftht==-1:
                return -1

            rightht = htcheck(root.right)
            if rightht ==-1:
                return -1

            if abs(rightht-leftht)>1:
                return -1

            return 1 + max(leftht, rightht)
        
        return htcheck(root)!=-1
