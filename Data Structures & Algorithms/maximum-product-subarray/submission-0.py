class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        m=max(nums)
        rp=1
        i=0
        j=i
        while i<=j:
            j=i
            rp=1
            while j<len(nums):
                if nums[j]==0:
                    j=j+1
                    rp=1
                else:
                    rp*=nums[j]
                    j+=1
                    m=max(m,rp)
            i+=1
        return m
        