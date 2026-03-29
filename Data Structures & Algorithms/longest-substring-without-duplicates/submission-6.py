class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m=0
        i=0
        if len(s)<2:
            return len(s)
        j=i
        sums=0
        d=defaultdict()
        while j<len(s):
            # print(d,m)
            if s[j] not in d:
                d[s[j]]=j
                sums+=1
                j+=1
            else:
                i=d[s[j]]+1
                j=i
                sums=0
                d=defaultdict()
            m=max(m,sums)
            
        return m
                

        