class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        cache = collections.defaultdict(list)

        for word in strs:
            alphabets = [0] * 26
            for st in word:
                alphabets[ord(st) - ord('a')] += 1
            cache[str(alphabets)].append(word)
        
        return list(cache.values())
            

        