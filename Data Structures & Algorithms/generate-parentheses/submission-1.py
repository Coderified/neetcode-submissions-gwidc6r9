class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        l =[]

        def bt(o,c):
            if o==c==n:
                print("result--",o,c,l)
                res.append("".join(l))
                return 

            if o<n:
                l.append("(")
                bt(o+1,c)
                l.pop()
                
            if c<o:
                l.append(")")
                bt(o,c+1)
                l.pop()
        
        bt(0,0)
        return res
        