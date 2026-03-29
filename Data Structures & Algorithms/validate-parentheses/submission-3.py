class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 !=0:
            return False
        else:
            l=[]
            d={"}":"{","]":"[",")":"("}
            for items in s:
                if items in d.values():
                    l.append(items)
                    s=s.replace(items,"")
                else:
                    if len(l)>0 and d[items]==l[-1]:
                        l.pop()
                        s=s.replace(items,"")
                    else:
                        return False
        return len(l)==0



        