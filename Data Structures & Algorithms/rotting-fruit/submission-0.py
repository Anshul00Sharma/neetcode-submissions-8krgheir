class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh,time = 0,0
        row,col = len(grid),len(grid[0])
        queue = deque()
        dirc = [[0,1],[1,0],[-1,0],[0,-1]] 

        # count the fresh oranges
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r,c))
        
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r,c = queue.popleft()

                for rb,cb in dirc:
                    rd = rb+r 
                    cd = cb+c
                    if rd >= 0 and rd < row and cd >= 0 and cd < col and grid[rd][cd] == 1:
                        grid[rd][cd] = 2
                        fresh -= 1
                        queue.append((rd,cd))
            time += 1
        return time if fresh == 0 else -1