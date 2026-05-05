class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        grid = collections.defaultdict(set)

        n = len(board)
        
        for r in range(n):
            for c in range(n):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in grid[(int(r/3),int(c/3))]):
                    return False 
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                grid[(r // 3,c // 3)].add(board[r][c])
        return True