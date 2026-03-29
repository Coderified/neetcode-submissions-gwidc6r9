class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)):
            c=c^nums[i]

        return c
            
        
        