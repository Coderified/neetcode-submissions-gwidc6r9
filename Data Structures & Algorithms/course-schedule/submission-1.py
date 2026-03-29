from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        d = defaultdict(list)
        inreturn = [0]*numCourses

        for crs, pre in prerequisites:
            d[pre].append(crs)
            inreturn[crs]+=1

        q=deque()
        
        for i in range(numCourses):
            if inreturn[i]==0:
                q.append(i)
        count=0
        while q:
            x = q.popleft()
            count+=1 

            for courses in d[x]:
                inreturn[courses]-=1

                if inreturn[courses]==0:
                    q.append(courses)
        
        return count==numCourses
            




        
        