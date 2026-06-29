class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        maps = {}
        ans = []
        for n in nums:
            if n in maps:
                maps[n] += 1
            else:
                maps[n] = 1
        for el in maps:
            freq[maps[el]].append(el)
        
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return ans