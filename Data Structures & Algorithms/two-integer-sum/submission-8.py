class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=[]
        for idx,val in enumerate(nums):
            d.append((val,idx))
        d.sort(key = lambda x:x[0])

        i=0
        j=len(nums)-1

        while i<j:
            if d[i][0]+d[j][0]==target:
                if d[i][1]<=d[j][1]:
                    return [ d[i][1] , d[j][1] ]
                else:
                    return [ d[j][1] , d[i][1] ] 
            elif d[i][0]+d[j][0]<target:
                i+=1
            else:
                j-=1

                
              



        