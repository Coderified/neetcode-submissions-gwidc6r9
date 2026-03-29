class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        l=[]
        i=0
        a=newInterval[0]
        b=newInterval[1]


        while i < len(intervals):
            its=intervals[i]
            if its[1]<a:
                l.append(its)
                i+=1
            else:
                break
        
        while i<len(intervals) and intervals[i][0]<=b:
            a = min(a,intervals[i][0])
            b=max(b,intervals[i][1])
            i+=1
        
        l.append([a,b])
        
        while i<len(intervals):
            l.append(intervals[i])
            i+=1
        
        return l
        