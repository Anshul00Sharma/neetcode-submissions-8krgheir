class Solution:
    def trap(self, height: List[int]) -> int:
        totalWater = 0
        l,r = 0, len(height)-1
        maxL,maxR = 0,0

        while l < r:
            if height[l] <= height[r]:
                maxL = max(maxL,height[l])
                totalWater += maxL - height[l]
                l += 1
            else:
                maxR = max(maxR,height[r])
                totalWater += maxR - height[r]
                r -= 1
        return totalWater 
                



        



