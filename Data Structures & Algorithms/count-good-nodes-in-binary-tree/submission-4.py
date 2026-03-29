# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        q=deque()
        counts = 0

        if not root:
            return counts
        
        mtn = root.val
        q.append((root,mtn))
        
        counts+=1
        

        while q:
            for i in range(len(q)):
                x,mtn=q.popleft()

                if x.left:

                    if mtn <= x.left.val:
                        counts+=1
                    
                        
                    q.append((x.left,max(mtn,x.left.val)))
                    
                    
                if x.right:
                    
                    if mtn <= x.right.val:
                        counts+=1
                    
                    q.append((x.right,max(mtn,x.right.val)))
                    
        return counts

                        