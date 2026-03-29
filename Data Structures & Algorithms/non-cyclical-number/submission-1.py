class Solution:
    def isHappy(self, n: int) -> bool:
        l=[]
        s=0
        while s!=1:
            s=0
            for chrs in str(n):
                print(chrs)
                s+=int(chrs)**2
            
            if s==1:
                return True
            elif s in l:
                return False
            else:
                l.append(s)
                n=s
            

        return False

        