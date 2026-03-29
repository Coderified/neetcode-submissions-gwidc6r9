class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        i=0
        used_array=len(nums)*[0] 

        def bt(i,l):
                    
            if i==len(nums):
                res.append(list(l))
                return
            
            for x in range(0,len(nums)):

                if used_array[x] == 0:

                    l.append(nums[x])
                    used_array[x]=1

                    bt(i+1,l)

                    l.pop()
                    used_array[x]=0
                    

           
        bt(0,[])
        return res
            
        
         