class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        cache = collections.defaultdict(list)

        for string in strs:
            charmap = [0] * 26
            for c in string:
                charmap[ord(c) - ord('a')] += 1
            cache[tuple(charmap)].append(string)
        
        return list(cache.values())