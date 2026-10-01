from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for st in strs:
            alphabets = [0] * 26
            for ch in st:
                alphabets[ord(ch) - ord("a")] += 1
            groups[str(alphabets)].append(st)
        return list(groups.values())
        




        