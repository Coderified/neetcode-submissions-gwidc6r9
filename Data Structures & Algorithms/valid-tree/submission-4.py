from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges)!=n-1:
            return False
        
        d=defaultdict(list)
        
        for st,en in edges:
            d[st].append(en)
            d[en].append(st)

        visited=set()
        q=deque()

        if n>0:
            q.append(0)
            visited.add(0)

        while q:
            x=q.popleft()
            for items in d[x]:
                if items not in visited:

                    q.append(items)
                    visited.add(items)
        return len(visited)==n

        

        



            
            
            


