class Solution:
    def numDecodings(self, s: str) -> int:
        # numbers 1-26
        # leading 0 unusable
        # 112---> 1 12, 11 2, 1 1 2
        if s=="" or s[0]=='0':
            return 0
        n=len(s)
        l=[0]*(n+1)
        l[0]=1

        for i in range(1,n+1):
            if s[i-1]!="0":
                l[i]+=l[i-1]
            if i>1:
                if 10<=int(s[i-2:i]) and int(s[i-2:i])<=26:
                    l[i]+=l[i-2]
        return l[-1]  



         


