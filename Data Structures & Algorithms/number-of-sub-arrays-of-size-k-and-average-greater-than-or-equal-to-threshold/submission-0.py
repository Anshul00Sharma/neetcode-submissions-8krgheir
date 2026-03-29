class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        queue = deque()
        ans = 0
        target = k * threshold

        for el in arr:
            queue.append(el)
            if len(queue) > k:
                queue.popleft()
            if len(queue) == k:
                if sum(queue) >= target:
                    ans += 1
        return ans