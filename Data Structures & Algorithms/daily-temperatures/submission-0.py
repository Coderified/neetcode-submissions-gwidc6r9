class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l=[0]*len(temperatures)
        for i in range(len(temperatures)):
            s=0
            j=i
            while j<len(temperatures):
                if temperatures[j]<=temperatures[i]:
                    j+=1
                else:
                    l[i]=(j-i)
                    break

                    
        return l
        