class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        subs = set()
        l = 0
        for st in s:
            while st in subs:
                subs.remove(s[l])
                l+=1
            subs.add(st)
            maxLength = max(len(subs),maxLength)
        return maxLength