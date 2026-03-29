class Solution:
    def rob(self, nums: List[int]) -> int:
        d=[]
        if nums==[]:
            return []
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        if len(nums)>2:
            d=[nums[0],max(nums[0],nums[1])]
            for i in range(2,len(nums)):
                
                d.append(max(d[i-1],nums[i]+d[i-2]))
        return d[-1]


        