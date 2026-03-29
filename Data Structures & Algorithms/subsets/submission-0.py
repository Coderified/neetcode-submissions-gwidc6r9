class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def bt(i,l):
            if i==len(nums):
                res.append(list(l))
                return
            l.append(nums[i])
            bt(i+1,l)
            
            l.pop()
            bt(i+1,l)

            

            
        l=[]
        i=0
        bt(i,l)

        return res
        
        