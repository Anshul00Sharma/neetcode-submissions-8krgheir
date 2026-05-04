class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        hashq = {}

        for el in nums:
            hashq[el] = 1 + hashq.get(el,0)
        
        for el in hashq:
            freq[hashq[el]].append(el)

        ans = []

        nk = k

        for i in range(len(freq) - 1, 0, -1):
            if nk > 0:
                if len(freq[i]) > 0:
                    for h in freq[i]:
                        if nk > 0:
                            ans.append(h)
                            nk -= 1
        
        return ans