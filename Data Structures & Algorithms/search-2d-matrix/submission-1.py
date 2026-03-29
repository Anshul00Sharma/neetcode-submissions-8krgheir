class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col = len(matrix[0]), len(matrix)

        outLow = 0
        outHigh = col - 1
        outMid = outHigh

        while outLow <= outHigh:
            outMid = (outLow + outHigh) // 2
            if target > matrix[outMid][-1]:
                outLow += 1
            elif target < matrix[outMid][0]:
                outHigh -= 1
            else:
                break
        if not outLow <= outHigh:
            return False
        inLow = 0
        inHigh = row - 1
        while inLow <= inHigh:
            mid = (inLow + inHigh) // 2
            if target < matrix[outMid][mid]:
                inHigh = mid - 1
            elif target > matrix[outMid][mid]:
                inLow = mid + 1
            else:
                return True
        return False