class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l=[]
        s=0

        for ops in operations:

            
            if ops == "+":
                l.append(l[-1]+l[-2])
                s+=l[-1]
            elif ops == "D":
                l.append(2*l[-1])
                s+=l[-1]
            elif ops == "C":
                s-=l[-1]
                l.pop()  
            else:
                l.append(int(ops))
                s+=int(ops)

        return s
        