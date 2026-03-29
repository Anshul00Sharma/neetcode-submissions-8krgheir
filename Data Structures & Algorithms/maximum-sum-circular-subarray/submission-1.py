class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalmax,globalmin = nums[0],nums[0]
        currentMax, currentMin = 0,0
        total = 0

        for el in nums:
            currentMax = max(currentMax + el,el)
            currentMin = min(currentMin + el,el)
            total += el
            globalmax = max(globalmax,currentMax)
            globalmin = min(globalmin,currentMin)
        return max(globalmax, total - globalmin) if globalmax > 0 else globalmax
