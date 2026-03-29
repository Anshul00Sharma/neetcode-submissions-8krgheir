class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        maxcount = 0
        def islandLen(grid,r,c):
            if not (0 <= r < row and 0 <= c < col) or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            ct = 1
            ct += islandLen(grid,r+1,c)
            ct += islandLen(grid,r,c+1)
            ct += islandLen(grid,r-1,c)
            ct += islandLen(grid,r,c-1)

            return ct 
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    count = islandLen(grid,r,c)
                    maxcount = max(count,maxcount)

        return maxcount