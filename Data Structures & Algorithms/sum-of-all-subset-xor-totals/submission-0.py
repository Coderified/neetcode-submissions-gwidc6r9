class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res=[]
        curr=[]
        t=0
        def bt(i):
            if i>=len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[i])
            bt(i+1)
            curr.pop()
            bt(i+1)
        bt(0)
        ll=[]
        for l in res:
            print(l)
            s=0
            for nums in l:
                s^=nums
            t+=s
        return t
        
        