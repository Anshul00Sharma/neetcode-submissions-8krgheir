class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1charfreq = [0] * 26
        s2charfreq = [0] * 26

        for s in s1:
            s1charfreq[ord(s) - ord('a')] += 1

        left,right = 0,0

        while right < len(s2):
            s2charfreq[ord(s2[right]) - ord('a')] += 1

            if right - left + 1 <= len(s1):
                if right - left + 1 == len(s1):
                    val = tuple(s1charfreq) == tuple(s2charfreq)
                    if val:
                        return True
                right += 1
            else:
                s2charfreq[ord(s2[left]) - ord('a')] -= 1
                s2charfreq[ord(s2[right]) - ord('a')] -= 1
                left += 1
        return False





        

        