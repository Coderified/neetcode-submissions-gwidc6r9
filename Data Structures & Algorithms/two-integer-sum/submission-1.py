class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        while i <(len(nums)):
            # if (target - nums[i]) in nums and target / nums[i] != 2 :
            #     return [i,nums.index(target - nums[i])]
            if (target - nums[i]) in nums[i+1:] :
                return [i,nums[i+1:].index(target - nums[i])+i+1]          
            i+=1

                
              



        