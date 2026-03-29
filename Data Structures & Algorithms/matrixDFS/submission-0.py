class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])

        def helper( grid: List[List[int]],visited:set,r:int,c:int) -> int:
            
            # basecase
            if min(r,c) < 0 or r == row or c == col or (r,c) in visited or grid[r][c] == 1:
                return 0
            if r == row - 1 and c == col - 1:
                return 1
            
            visited.add((r,c))

            count = 0
            count += helper(grid,visited,r + 1,c)
            count += helper(grid,visited,r ,c+1)
            count += helper(grid,visited,r-1 + 1,c)
            count += helper(grid,visited,r ,c-1)

            visited.remove((r,c))

            return count
        return helper(grid,set(),0,0)
        



        