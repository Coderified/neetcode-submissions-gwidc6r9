# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q=deque()
        res=[]
        level=0
        q.append(root)

        while q:
            y=len(q)

            for i in range(len(q)):
                
                
                x=q.popleft()
                # print(x.val,y)
                if i==y-1:
                    res.append(x.val)
                
                
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
        return res
            
        