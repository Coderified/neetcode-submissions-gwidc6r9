class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c=[0]*3

        for num in nums:
            c[num]+=1
        
        stidx=0

        for idx in range(len(c)):
            noftimes = c[idx]
            print(idx,noftimes,stidx)
            for i in range(stidx,noftimes+stidx):
                nums[i]=idx 
            stidx += noftimes
        return nums





        