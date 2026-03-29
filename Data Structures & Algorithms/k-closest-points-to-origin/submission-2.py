class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l=[]

        for x,y in points:
            val = ((x**2)+(y**2))
            key = (x,y)
            l.append((val,key))
        heapq.heapify(l)
        ll=[]

        for x in range(k):
            ll.append(heapq.heappop(l)[1])
        return ll

        