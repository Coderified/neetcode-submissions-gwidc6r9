class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        res=0
        
        i=0
    

        for j in range(len(s)):

            
            
            cha = s[j]
            d[cha]=d.get(cha,0)+1

            

            if (j-i+1) - max(d.values())>k:
                cha=s[i]
                d[cha]-=1
                i+=1
            res = max(res,j-i+1)
            print("i,j",i,j)
            print("d",d)
            print(res)

        return res