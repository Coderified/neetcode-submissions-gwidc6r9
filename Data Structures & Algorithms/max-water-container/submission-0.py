class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m=0
        i=0
        j=len(heights)-1

        while i<j:
            prod = min(heights[i],heights[j])*(j-i)
            m=max(m,prod)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return m
            
        