class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        res=nums[0]
        
        while l<r:
            mids = (l+r)//2
            if nums[l]<=nums[mids]:
                l=mids+1
                
            elif nums[mids] <= nums[l]:
                r=mids
                
            
            res = min(res,nums[l])
        return res

        

        