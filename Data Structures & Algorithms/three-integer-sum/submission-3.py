class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        l=[]
        n=len(nums)
        i=0
        while i < n:
            if i>0 and nums[i]==nums[i-1]:
                i+=1
            else:
                target = -nums[i]
                s=i+1
                e=n-1
                while s<e:
                    
                    if nums[s]+nums[e] == target:
                        while s<e and nums[s]==nums[s+1]:
                            s+=1
                        while s<e and nums[e]==nums[e-1]:
                            e-=1
                        l.append([nums[i],nums[s],nums[e]])
                        s+=1
                        e-=1
                    elif nums[s]+nums[e] < target:
                        s+=1
                    else:
                        e-=1
                i+=1
            
        return l