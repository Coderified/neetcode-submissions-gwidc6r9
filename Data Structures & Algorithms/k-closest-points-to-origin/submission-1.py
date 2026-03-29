class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d={}
        l=[]
        for x,y in points:
            
            d[(x,y)]=(((x**2)++(y**2))**0.5)
        
        l=[(value,key) for key,value in d.items()]
        heapq.heapify(l)
        print(l)
        ll=[]
        while l:
            ll.append(heapq.heappop(l)[1])
        return ll[0:k]

        