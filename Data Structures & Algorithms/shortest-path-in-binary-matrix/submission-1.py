class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row ,col = len(grid),len(grid[0])
        if grid[0][0] == 1 or grid[row-1][col-1] == 1:
            return -1

        queue = deque([(0, 0, 1)])
        grid[0][0] = 1

        while len(queue) > 0:
           r, c, path = queue.popleft()
           if r == row - 1 and c == col - 1:
               return path

           directions = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]

           for br,bc in directions:
            nr, nc = r + br, c + bc
            if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                grid[nr][nc] = 1
                queue.append((nr, nc, path + 1))
        return -1