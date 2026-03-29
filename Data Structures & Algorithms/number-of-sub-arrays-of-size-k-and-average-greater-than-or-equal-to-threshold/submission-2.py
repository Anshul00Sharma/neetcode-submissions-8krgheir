class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        currentSum = 0
        l = 0
        ans = 0
        targetSum = k * threshold

        for r in range(len(arr)):
            currentSum += arr[r]
            if r - l + 1 > k:
                currentSum -= arr[l]
                l += 1
            if r - l + 1 == k and currentSum >= targetSum:
                ans += 1
            

        return ans