class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROW = [set() for _ in range(9)]
        COL = [set() for _ in range(9)]
        GRID = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                element = board[r][c]
                if element == ".":
                    continue
                if element in ROW[r] or element in COL[c] or element in GRID[r // 3][c // 3]:
                    return False
                ROW[r].add(element)
                COL[c].add(element)
                GRID[r // 3][c // 3].add(element)
        return True 
        