class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
         
        print(nums)      
        s=set((nums))
        
        s=list(s)
        s.sort()
        c=0
        maxs=0
        print(s)
        for i in range(len(s)-1):
            if s[i+1]-s[i]==1:
                c+=1
                maxs = max(maxs,c)
            else:
                c=0 
        if len(nums)>0:
            return maxs+1
        else:
            return 0


        