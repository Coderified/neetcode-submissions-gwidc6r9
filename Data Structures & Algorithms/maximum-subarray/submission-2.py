class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        s=0
        maxs = max(nums)

        for i in range(len(nums)):
            s= max(s+nums[i],nums[i])
            maxs = max(maxs,s)
        return maxs
        