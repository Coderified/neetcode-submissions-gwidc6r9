class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums.reverse()
        
        k=k%len(nums)
        
        def rev(i,j):
            while i<j:
                # print('first loop',i,j)
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        rev(0,k-1)
        rev(k,len(nums)-1)
        
        