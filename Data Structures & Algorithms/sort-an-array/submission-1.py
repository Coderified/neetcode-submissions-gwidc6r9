class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums)<=1:
            return nums
        
        mids = len(nums)//2
        l = self.sortArray(nums[:mids])
        r = self.sortArray(nums[mids:])

        return self.merge_logic(l,r)

    def merge_logic(self,l,r):
        i,j=0,0
        res=[]

        while i<len(l) and j<len(r):

            if l[i]<r[j]:
                res.append(l[i])
                i+=1
            else:
                res.append(r[j])
                j+=1
        
        res.extend(l[i:])
        res.extend(r[j:])

        return res

