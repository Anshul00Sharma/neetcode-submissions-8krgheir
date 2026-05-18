class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        p1,p2=0,0
        count = [0] * 26
        length = 0

        while p2 < len(s):
            count[ord(s[p2]) - ord("A")] += 1
            windowlength = p2 - p1 + 1

            maxcount = max(count) 
            if (windowlength - maxcount) <= k:
                length = max(length,windowlength)
                p2 += 1
            else:
                count[ord(s[p2]) - ord("A")] -= 1
                count[ord(s[p1]) - ord("A")] -= 1
                p1 += 1
        return length