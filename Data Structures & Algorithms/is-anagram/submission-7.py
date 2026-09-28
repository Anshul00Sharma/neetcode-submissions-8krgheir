class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        alphabetsS = [0] * 26
        alphabetsT = [0] * 26

        for index in range(len(s)):
            alphabetsS[ord(s[index]) - ord('a')] += 1
            alphabetsT[ord(t[index]) - ord('a')] += 1
        return str(alphabetsS) == str(alphabetsT)    



        