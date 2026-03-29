from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        d=defaultdict(list)

        for a,b in edges:
            d[a].append(b)
            d[b].append(a)

        q=deque([0])
        visited = set()
        visited.add(0)
        l=0

        while len(visited)<n:
            if len(q)==0:
                for i in range(n):
                    if i not in visited:
                        q.append(i) 
                        visited.add(i)
                        break
                        
            while q:
                x=q.popleft()
                if x not in d:
                    pass
                    
                else:    
                    for items in d[x]:
                        if items not in visited:
                            visited.add(items)
                            if items not in q:
                                q.append(items)
            print(visited,q,n)
            l+=1
     
        return l
        


        