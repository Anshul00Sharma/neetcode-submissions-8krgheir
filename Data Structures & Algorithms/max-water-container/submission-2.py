class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areamax = 0
        p1 = 0
        p2 = len(heights) - 1
        while p1 < p2:
            width = p2 - p1
            height = min(heights[p1],heights[p2])
            areamax = max(areamax,width * height)
            if (heights[p1] < heights[p2]):
                p1+= 1
            else:
                p2-= 1
        return areamax
        