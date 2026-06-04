class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # find the row
        start = 0
        end = len(matrix) - 1
        targetRow = 0

        while start <= end:
            mid = (start + end) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                targetRow = mid
                break
            elif matrix[mid][0] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        # find target in the row
        s,e = 0 , len(matrix[0])-1

        while s <= e:
            mid = (s + e) // 2
            if matrix[targetRow][mid] == target:
                return True
            elif matrix[targetRow][mid] < target:
                s = mid + 1
            else:
                e = mid - 1
        return False