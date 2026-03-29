class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)<3:
            return max(nums)
        else:    
            def cal(nums):
                
                l=[nums[0],max(nums[0],nums[1])]

                for i in range(2,len(nums)):
                    l.append(max(l[i-1],nums[i]+l[i-2]))
                
                return max(l)
            
            ominus = cal(nums[:-1])
            oplus = cal(nums[1:])   
            return (max(ominus,oplus))
            