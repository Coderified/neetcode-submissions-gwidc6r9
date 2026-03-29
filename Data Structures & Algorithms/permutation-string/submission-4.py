class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i=0
        j=len(s1)-1
        c=0
        d1 = defaultdict(int)
        
        d2 = defaultdict(int)

        if len(s2)<len(s1):
            return False
        for x in range(len(s1)):
            
            d1[s1[x]]+=1
            d2[s2[x]]+=1
        a=j
        while a<len(s2):
            print(a)
            print(a,d1,d2)
            if d1==d2:
                return True
            elif a==len(s2)-1 and d1!=d2:
                return False
            else:
                d2[s2[a-len(s1)+1]]-=1
                if d2[s2[a-len(s1)+1]]==0:
                    del d2[s2[a-len(s1)+1]]
                a+=1
                d2[s2[a]]+=1
        return False




        