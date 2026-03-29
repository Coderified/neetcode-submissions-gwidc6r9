class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        s=nums[0]

        i=0
        while i<len(nums):
            
            for j in range(i+1,len(nums)+1):
                s=max(s,sum(nums[i:j]))
                print(nums[i:j])
            i+=1
        return s

        