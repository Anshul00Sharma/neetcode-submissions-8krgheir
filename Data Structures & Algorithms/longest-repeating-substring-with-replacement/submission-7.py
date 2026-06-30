class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left,right= 0,0
        count = [0] * 26
        maxcount = 0

        while right < len(s):
            count[ord(s[right]) - ord('A')] += 1
            windowSize = right - left + 1

            maxchar = max(count)

            if windowSize - maxchar <= k:
                maxcount = max(maxcount,windowSize)
                right+=1
            else:
                count[ord(s[left]) - ord('A')] -= 1
                count[ord(s[right]) - ord('A')] -= 1
                left += 1
        return maxcount



        