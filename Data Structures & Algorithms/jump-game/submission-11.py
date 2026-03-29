class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        m=0

        for i in range(len(nums)):

            if i>m:
                return False

            if m>=len(nums)-1:
                return True
            m = max(i+nums[i],m)




        # while i<len(nums):
        #     print(i)

        #     if nums[i]==0 and i <len(nums)-1:
        #         return False
        #     if i>=len(nums)-1 or len(nums)-i<=nums[i]:
        #         return True
        #     mj=0
        #     maxs=0
        #     for y in range(i+1,i+nums[i]+1):
        #         maxs = max(maxs,nums[y]-len(nums)-y)
        #         if y>=len(nums)-1 or len(nums)-y<=nums[y]:
        #             return True
        #         if mj<=maxs:
        #             mj=maxs
        #             i=y
                
            
