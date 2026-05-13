class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colhash = [set() for _ in range(9)]
        rowhash = [set() for _ in range(9)]
        gridhash = [[set() for _ in range(3)] for _ in range(3)] 

        for r in range(9):
            for c in range(9):
                element = board[r][c]
                if element == ".":
                    continue
                
                if (element in rowhash[r] or 
                    element in colhash[c] or 
                    element in gridhash[r // 3][c // 3]):
                    return False
                
                rowhash[r].add(element)
                colhash[c].add(element)
                gridhash[r // 3][c // 3].add(element)
        
        return True