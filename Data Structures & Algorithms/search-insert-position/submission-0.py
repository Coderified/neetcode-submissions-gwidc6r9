class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1

        if target<nums[0]:
            return 0
        if target>nums[j]:
            return j+1

        while i<j:
            mid = (i+j)//2

            if target<=nums[mid]:
                j=mid
            else:
                i=mid+1
        if target<=nums[i]:
            return i
        else:
            return i+1
