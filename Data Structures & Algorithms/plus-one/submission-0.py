class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=0
        l=[]
        s=0
        while i<=len(digits)-1:
            s= (10*s + digits[i] )
            i+=1
        s+=1
        for chars in str(s):
            l.append(int(chars))
        return l
        