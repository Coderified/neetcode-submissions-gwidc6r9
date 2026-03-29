class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q=deque()
        i=0
        for i in range(len(tokens)):
            # print(q)
            
            if tokens[i] not in ("+", "-", "*", "/") :
                q.append(tokens[i])
            else:
                a=int(q.pop())
                b=int(q.pop())
                if tokens[i]=="+":
                    q.append(a+b)
                elif tokens[i]=="-":
                    q.append(b-a)
                elif tokens[i]=="*":
                    q.append(a*b)
                elif tokens[i]=="/":
                    q.append((b/a))
        return int(q[0])

        