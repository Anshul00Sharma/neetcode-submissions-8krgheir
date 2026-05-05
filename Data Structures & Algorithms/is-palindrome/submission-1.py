class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1,p2=0,len(s)-1
        valid ="abcdefghijklmnopqrstuvwxyz01234546789"

        while p1 < p2:
            if s[p1].lower() not in valid:
                p1 +=1
                continue
            if s[p2].lower() not in valid:
                p2 -=1
                continue
            
            if s[p1].lower() != s[p2].lower():
                return False
            p1 += 1
            p2 -= 1
        return True