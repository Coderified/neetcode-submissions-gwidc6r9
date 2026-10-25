class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges)!=n-1:
            return False

        adj_list = [[] for i in range(n)]
        
        #Undirected adjacency list
        for st,end in edges:
            adj_list[st].append(end)
            adj_list[end].append(st)
             
        
        q=deque()
        visited=set()

        q.append(0)
        visited.add(0)

        while q:
            a=q.popleft()
            dependents = adj_list[a]
            
            for ends in dependents:
                if ends not in visited:
                    visited.add(ends)
                    q.append(ends)
        
        return len(visited)==n

        