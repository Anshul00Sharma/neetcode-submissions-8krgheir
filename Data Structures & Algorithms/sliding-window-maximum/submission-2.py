class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()

        l = r = 0
        ans = []

        while r < len(nums):
            while queue and nums[r] > nums[queue[-1]]:
                queue.pop()
            queue.append(r)

            if l > queue[0]:
                queue.popleft()
            
            if r >= k - 1:
                ans.append(nums[queue[0]])
                l += 1
            r += 1
        return ans
