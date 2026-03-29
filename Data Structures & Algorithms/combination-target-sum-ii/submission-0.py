class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res=[]
        candidates.sort()

        def bt(i,s,l):
            if target==s:
                res.append(list(l))
                return
            if i==len(candidates) or s>target:
                return
            
            
        
            l.append(candidates[i])
            
            
            bt(i+1,s+candidates[i],l)

            l.pop()
            while i+1<len(candidates) and candidates[i+1]==candidates[i]:
                i+=1
            
            bt(i+1,s,l)

        bt(0,0,[])
        return res
        