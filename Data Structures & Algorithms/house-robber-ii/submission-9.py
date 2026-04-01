class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)    
        
        
        dp1=[0]*(len(nums)-1)

        dp1[0]=nums[0]
        dp1[1] = max(nums[0:2])

        for x in range(2,len(nums)-1):
            dp1[x] = max(dp1[x-1],dp1[x-2]+nums[x])
        

        dp2 = [0]*(len(nums)-1)
        dp2[0] = nums[1]
        dp2[1] = max(nums[1:3])

        for x in range(3,len(nums)):
            dp2[x-1] = max(dp2[x-2],dp2[x-3]+nums[x])

        return max(dp1[-1],dp2[-1])