import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        for subArr in points:
            val = subArr[0] ** 2 + subArr[1] ** 2
            arr.append((val, subArr))
        heapq.heapify(arr)
        ans = []
        for _ in range(k):
            val, point = heapq.heappop(arr)
            ans.append(point)
        return ans