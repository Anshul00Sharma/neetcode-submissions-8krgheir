class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = high
        while low <= high:
            mid = (low + high) // 2
            hours = 0
            for el in piles:
                hours += math.ceil(el/mid)
            if hours > h:
                low = mid + 1
            else:
                res = mid
                high = mid - 1
        return res

        