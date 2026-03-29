class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for nums in matrix:
            if nums[-1]>=target >=nums[0]:
                i,j=0,len(nums)-1

                while i<=j:
                    m=(i+j)//2

                    if target==nums[m]:
                        return True

                    elif nums[i]<=target and target<nums[m]:
                        j=m-1
                    else:
                        i=m+1
        return False    