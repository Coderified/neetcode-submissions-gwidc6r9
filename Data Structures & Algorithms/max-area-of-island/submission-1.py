class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m=0
        rows,cols = len(grid),len(grid[0])

        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0:
                return 0
            grid[r][c]=0

            return (1 + dfs(r,c+1)+ dfs(r,c-1)+ dfs(r+1,c)+ dfs(r-1,c))

        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y]==0:
                    continue
                else:
                    
                    m=max(m,dfs(x,y))

        return m
        