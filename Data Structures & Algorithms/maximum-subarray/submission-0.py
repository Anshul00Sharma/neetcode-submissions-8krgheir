class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentmax = 0

        for el in nums:
            currentmax = max(currentmax, 0)
            currentmax += el
            maxSum = max(currentmax, maxSum)
        return maxSum