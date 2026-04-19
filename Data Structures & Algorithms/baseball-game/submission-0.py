class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l=[]

        for ops in operations:

            
            if ops == "+":
                l.append(l[-1]+l[-2])
            elif ops == "D":
                l.append(2*l[-1])
            elif ops == "C":
                l.pop()
            else:
                l.append(int(ops))

        return sum(l)
        