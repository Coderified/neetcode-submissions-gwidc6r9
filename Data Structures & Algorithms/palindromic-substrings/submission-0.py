class Solution:
    def countSubstrings(self, s: str) -> int:
        l=[]
        def ps(i,j,s):
            c=0
            while(i>=0 and j<len(s) and s[i]==s[j]):
                c+=1
                i-=1
                j+=1
            return c

        for x in range(0,len(s)):
            l.append(ps(x,x,s))
            l.append(ps(x,x+1,s))
            
        return sum(l)
        