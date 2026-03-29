class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def bound(flag):
            i=0
            j=len(nums)-1
            bound=-1

            while i<=j:
                mids = (i+j)//2

                if target==nums[mids]:
                    bound = mids

                    if flag == True:
                        j=mids-1
                    else:
                        i=mids+1
                elif target>nums[mids]:
                    i=mids+1
                else:
                    j=mids-1
            return bound
        
        return [bound(True),bound(False)]


        