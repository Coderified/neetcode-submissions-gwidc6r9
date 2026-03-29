class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res: List[List[int]] = []

        def dfs(i,cur,total):

            if total==target:
                res.append(cur.copy())
                return 
            
            if i == len(nums) or total>target:
                return 
        
            if total+nums[i]<=target:
                cur.append(nums[i])
                dfs(i,cur,total+nums[i])
                cur.pop()

            dfs(i+1,cur,total)

        dfs(0,[],0)    
        return res
        
        




        