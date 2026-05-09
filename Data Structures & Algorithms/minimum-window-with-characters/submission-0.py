class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = 0
        need = len(needdict := Counter(t))
        havedict = {}
        minimumsubstring = float('inf')
        subString = ""

        l = 0
        
        for r in range(len(s)):
            char = s[r]
            havedict[char] = 1 + havedict.get(char, 0)
            if char in needdict and havedict[char] == needdict[char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < minimumsubstring:
                    minimumsubstring = (r - l) + 1
                    subString = s[l:r+1]
                
                left_char = s[l]
                havedict[left_char] -= 1
                if left_char in needdict and havedict[left_char] < needdict[left_char]:
                    have -= 1
                l += 1
        return subString