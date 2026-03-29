class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1

        while i<j:
            mid = (i+j)//2

            if target<=nums[mid]:
                j=mid
            else:
                i=mid+1
        if i==j:
            if target ==nums[i]:
                return i
            else:
                return -1
        