class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        s=max(nums)
        t=nums[0]
        
        for i in range(1,len(nums)):
            t = max (nums[i]+t,nums[i])

            s=max(s,t)
        return s