from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = [[] for i in range(numCourses)]
        in_degree = [0]*numCourses
        taken=0

        # map graph in adj_list
        for c,pr in prerequisites:
            adj_list[pr].append(c)
            in_degree[c]+=1
        
        q=deque()
        for x in range(numCourses):
            if in_degree[x]==0:
                q.append(x)
        
        while q:
            i=q.popleft()
            taken+=1
            dependents = adj_list[i]
            
            for cs in dependents:
                in_degree[cs]-=1
                if in_degree[cs]==0:
                    q.append(cs)
                
        return taken==numCourses



        


             
                
            

        