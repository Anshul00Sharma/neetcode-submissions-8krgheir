class Solution:
    def trap(self, height: List[int]) -> int:
        maxL,maxR = 0,0
        l,r = 0, len(height) - 1
        traped = 0
        while l < r:
            if height[l] < height[r]:
                maxL = max(maxL,height[l])
                traped += max(maxL - height[l],0)
                l += 1 
            else:
                maxR = max(maxR,height[r])
                traped += max(maxR - height[r],0)
                r -= 1
        return traped

        