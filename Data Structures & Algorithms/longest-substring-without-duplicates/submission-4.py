class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        subs = []
        for st in s:
            while st in subs:
                subs.pop(0)
            subs.append(st)
            maxLength = max(len(subs),maxLength)
        return maxLength