class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
 
        dist = collections.defaultdict(list)

        for strings in strs:
            alphabets = [0] * 26
            for alpha in strings:
                alphabets[ord(alpha.lower()) - ord('a')] += 1
            dist[tuple(alphabets)].append(strings)
        
        return list(dist.values())

        