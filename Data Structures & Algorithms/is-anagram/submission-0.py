class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        d={}
        for letters in s:
            d[letters] = d.get(letters,0)+1

        for letters in t:
            if letters not in d:
                return False
            else:
                d[letters] -=1
            if d[letters]<0:
                return False
        return True 


        
        
        