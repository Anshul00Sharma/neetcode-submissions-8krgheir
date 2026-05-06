class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        n = len(heights)
        p1,p2 = 0,n-1

        while p1 < p2:
            if heights[p1] < heights[p2]:
                maxA = max(maxA,heights[p1] * (p2-p1))
                p1 += 1
                
            else:
                maxA = max(maxA,heights[p2] * (p2-p1)) 
                p2 -= 1
                
        
        return maxA