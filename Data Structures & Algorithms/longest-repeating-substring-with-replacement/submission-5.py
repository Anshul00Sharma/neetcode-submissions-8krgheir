class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        p1,p2 = 0,0
        n = len(s)
        count = [0] * 26
        ans = 0

        while p2 < n:
            count[ord(s[p2]) - ord('A')] += 1
            maxsize = max(count)
            if p2-p1 + 1 - maxsize <= k:
                ans = max(ans,p2-p1 + 1)
                p2 += 1
            else:
                count[ord(s[p2]) - ord('A')] -= 1
                count[ord(s[p1]) - ord('A')] -= 1
                p1 += 1
        return ans