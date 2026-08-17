class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        l = [x for x in range(1,n+1)]
        res=[]
        curr=[]
        def bt(i):
            if len(curr)==k:
                res.append(curr.copy())
                return
            if i>=n:
                return
            curr.append(l[i])
            bt(i+1)
            curr.pop()
            bt(i+1)
        bt(0)
        return res

            



        