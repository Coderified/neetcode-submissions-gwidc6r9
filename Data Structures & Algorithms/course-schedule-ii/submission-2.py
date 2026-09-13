from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj_list = [[] for _ in range(numCourses)]
        in_deg = [0]* numCourses
        l=[]

        for c,pr in prerequisites:
            adj_list[pr].append(c)
            in_deg[c]+=1
        
        q = deque()

        for c in range(numCourses):
            if in_deg[c]==0:
                q.append(c)
        
        while q:
            x = q.popleft()
            l.append(x)

            for dependents in adj_list[x]:
                in_deg[dependents]-=1

                if in_deg[dependents]==0:
                    q.append(dependents)
        if len(l)==numCourses:
            return l
        else:
            return []



        