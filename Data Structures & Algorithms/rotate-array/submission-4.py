class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums.reverse()
        
        k=k%len(nums)
        i=0
        j=k-1

        while i<j:
            # print('first loop',i,j)
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
        i=k
        j=len(nums)-1
        while i<j:
            # print('2nd loop',i,j)
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
        
        
        