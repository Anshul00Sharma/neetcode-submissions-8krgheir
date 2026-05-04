class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for el in strs:
            count = [0] * 26

            for c in el:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(el)
        
        return list(res.values())