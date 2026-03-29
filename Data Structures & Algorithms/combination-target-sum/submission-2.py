class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        s=0
        res=[]
        def bt(i,s,l):

            if s > target or i == len(nums):
                return

            if s==target:
                res.append(list(l))
                return 
            
            l.append(nums[i])
            bt(i,s+nums[i],l)

            l.pop() 
            bt(i+1,s,l)
        l=[]
        bt(0,0,l)

        return res

        