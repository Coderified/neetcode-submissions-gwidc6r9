# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        def dfs(root):
            if root is None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            ht = 1 + max(left,right)

            return ht

        leftht=dfs(root.left)
        rightht = dfs(root.right)

        if abs(rightht-leftht)>1:
            return False


        return self.isBalanced(root.left) & self.isBalanced(root.right)



