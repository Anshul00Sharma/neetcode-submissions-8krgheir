class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(arr):
            max_s = cur = arr[0]
            for x in arr[1:]:
                cur = max(x, cur + x)
                max_s = max(max_s, cur)
            return max_s

        def min_kadane(arr):
            min_s = cur = arr[0]
            for x in arr[1:]:
                cur = min(x, cur + x)
                min_s = min(min_s, cur)
            return min_s

        total = sum(nums)
        max_linear = kadane(nums)
        min_linear = min_kadane(nums)
        
        if total == min_linear:
            return max_linear
        return max(max_linear, total - min_linear)