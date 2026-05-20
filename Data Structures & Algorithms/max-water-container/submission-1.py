class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWaterArea = 0
        left,right = 0,len(heights)-1

        while left < right:
            if heights[left] <= heights[right]:
                maxWaterArea = max(maxWaterArea, (right-left) * heights[left])
                left +=1
            else:
                maxWaterArea = max(maxWaterArea, (right-left) * heights[right])
                right -=1
        
        return maxWaterArea

        