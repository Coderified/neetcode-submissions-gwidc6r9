class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxs=0
        c=0
        i=0
        if len(s)==1:
            return 1
        else:
            while i<len(s):
                c=0
                j=i   
                l=[]    
                while j < len(s):
                    
                    if s[j] not in l:
                        c+=1
                        l.append(s[j])
                        j+=1
                        maxs = max(maxs,c)
                    else:
                                             
                        break
                i+=1
            return maxs



        