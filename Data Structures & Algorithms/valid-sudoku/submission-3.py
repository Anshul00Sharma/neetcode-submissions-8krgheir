class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        grid = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                element = board[r][c]
                if element == ".":
                    continue
                if element in row[r] or element in col[c] or element in grid[r // 3][c // 3]:
                    return False
                row[r].add(element)
                col[c].add(element)
                grid[r // 3][c // 3].add(element)

        return True