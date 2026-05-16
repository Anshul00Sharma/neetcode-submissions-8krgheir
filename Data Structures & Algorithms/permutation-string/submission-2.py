class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        r =  len(s1) - 1

        askis1 = [0] * 26
        for char in s1:
            askis1[ord(char) - ord('a')] += 1

        while r < len(s2):
            askis2 = [0] * 26

            for char in s2[l:r+1]:
                askis2[ord(char) - ord('a')] += 1
            if tuple(askis2) == tuple(askis1):
                return True
            l += 1
            r += 1
        return False


        
        