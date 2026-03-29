import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m=max(piles)
        n=len(piles)

        if h==n:
            return m
        else:
            i=1
            j=m
            res=int()
            while i<=j:

                mid = (i+j)//2
                s=0
                for x in range(n):
                    s+=int(math.ceil(piles[x]/mid))
                if s<=h:
                    res=mid
                    j=mid-1
                else:
                    i=mid+1 
                
            return res