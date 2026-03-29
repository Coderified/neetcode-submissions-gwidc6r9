"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if len(intervals)==1:
            return 1

        st=[]
        en=[]

        for items in intervals:
            st.append(items.start)
            en.append(items.end)
        
        st.sort()
        en.sort()

        c=0
        m=0
        s=0
        e=0

        while s<len(st):
            if st[s]<en[e]:
                c+=1
                s+=1
            else:
                e+=1
                c-=1

            
            m=max(m,c)
        return m
            
            
                
            

        

        
        
        