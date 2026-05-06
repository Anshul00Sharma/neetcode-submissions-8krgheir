class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        pL,pR=0,n-1
        maxL , maxR = height[pL],height[pR]
        total = 0
        
        while pL < pR:
            if height[pL] < height[pR]:
                if maxL - height[pL] > 0:
                    total += maxL - height[pL]
                maxL = max(maxL,height[pL])
                pL += 1
            else:
                if maxR - height[pR] > 0:
                    total += maxR - height[pR]
                maxR = max(maxR,height[pR])
                pR -= 1
        return total



