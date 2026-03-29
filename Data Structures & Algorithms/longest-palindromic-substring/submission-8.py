class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=[]
        if len(s)==1:
            return s
        if len(s)==2:
            if s[0]==s[1]:
                return s
            else:
                return s[0]
        def opal(i,s):
            k=1
            while i-k>=0 and i+k<len(s) and s[i-k]==s[i+k]:
                print("Checking-->",i,k,s[i-k],s[i+k])
                k+=1
            k-=1
            return s[i-k:i+k+1]
        def epal(i,j,s):
            k=0
            while i-k>=0 and j+k<len(s) and s[i-k]==s[j+k]:
                k+=1
            k-=1
            return s[i-k:j+k+1]
        for i in range(0,len(s)-1):
            l.append(epal(i,i+1,s))
            print("l even is",l)
    
        for i in range(0,len(s)-1):
            l.append(opal(i,s))
            print("l odd is",l)
        return max(l, key=len)

            



        