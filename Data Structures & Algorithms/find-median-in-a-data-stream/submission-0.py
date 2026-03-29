class MedianFinder:

    def __init__(self):
        self.l = []
        

    def addNum(self, num: int) -> None:
        self.l.append(num)
        

    def findMedian(self) -> float:
        self.l.sort()

        x = len(self.l)
        if x%2 != 0:
            return self.l[x//2]
        else:
            a=int(x/2)
            return (self.l[a-1]+self.l[a])/2
             
        
        