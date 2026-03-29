class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        rtc=list(target-x for x in position)
        times = [x/y for x,y in zip(rtc,speed)]
        l=[]
        for i in range(len(position)):
            l.append([position[i],times[i]])
        l.sort(reverse=True)
        s=1
        print(l)
        for i in range(1,len(l)):
            
            if l[i][1] <= l[i-1][1]:
                l[i][1]=l[i-1][1]
                continue
            else:
                s+=1
        return s 

        



        
        