class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n==1:
            return x
        if n==-1:
            return 1/x

        a=1
        if n>0:
            y=x
            while a<n:

                y*=x
                a+=1
        else:
            y=(1/x)
            while a<abs(n):
                y*=(1/x)
                a+=1
        return y

        
        