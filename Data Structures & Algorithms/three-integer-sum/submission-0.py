class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        l=[]
        for i in range(len(nums)):
            target = -(nums[i])
            # l1=[]
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[j]+nums[k]==target:
                    if [-1*target,nums[j],nums[k]] not in l:
                        l.append([-1*target,nums[j],nums[k]])
                    j+=1
                    k-=1
                elif nums[j]+nums[k]<target:
                    j+=1
                elif nums[j]+nums[k]>target:
                    k-=1 

        return l
            

            








        