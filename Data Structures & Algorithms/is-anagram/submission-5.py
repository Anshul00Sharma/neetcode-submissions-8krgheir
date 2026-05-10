class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        have = [0] * 26
        need = [0] * 26

        for i in range(len(s)):
            have[ord(s[i].lower()) - ord('a')] += 1
            need[ord(t[i].lower()) - ord('a')] += 1
        return tuple(have) == tuple(need)

