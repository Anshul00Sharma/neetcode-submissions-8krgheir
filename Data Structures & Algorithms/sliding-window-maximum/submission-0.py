class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        l = 0
        r = k - 1
        ans = []
        

        while r < len(nums):
            ans.append(max(nums[l:r+1]))
            l += 1
            r += 1
        return ans


        