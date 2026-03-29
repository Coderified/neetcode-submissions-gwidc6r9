class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res=[]
        nums.sort()
        l=[]
        def bt(i,l):
            if i==len(nums):
                res.append(list(l))
                return
        # considering the number at i    
            l.append(nums[i])
            bt(i+1,l)
            l.pop()

        # skipping the no. at i
            while i+1<len(nums) and nums[i+1]==nums[i]:
                i+=1
            bt(i+1,l)
            
        bt(0,l)
        return res

        