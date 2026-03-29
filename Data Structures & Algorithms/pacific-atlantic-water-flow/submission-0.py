class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        l=[]
        p=set()
        a=set()

        rows = len(heights) 
        cols = len(heights[0])

        def dfs(r,c,reachable_set,prev_height):
            if (r, c) in reachable_set or r<0 or c<0 or r==rows or c==cols or heights[r][c]<prev_height:
                return
            reachable_set.add((r,c))

            dfs(r+1,c,reachable_set,heights[r][c])
            dfs(r-1,c,reachable_set,heights[r][c])
            dfs(r,c+1,reachable_set,heights[r][c])
            dfs(r,c-1,reachable_set,heights[r][c])

        for r in range(rows):
            dfs(r,0,p,heights[r][0])
            dfs(r,cols-1,a,heights[r][cols-1])

        
        for c in range(cols):
            dfs(0,c,p,heights[0][c])
            dfs(rows-1,c,a,heights[rows-1][c])
    
        for x in a:
            if x in p:
                l.append(x)
        return l


        