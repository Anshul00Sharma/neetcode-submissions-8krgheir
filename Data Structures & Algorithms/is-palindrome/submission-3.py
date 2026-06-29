class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1
        while(p1 < p2):
            if not self.valid(s[p1].lower()):
                p1+=1
                continue
            if not self.valid(s[p2].lower()):
                p2-=1
                continue
            if s[p1].lower() != s[p2].lower():
                return False
            p1+=1
            p2-=1
        return True 
            
                

              
    
    def valid(self, s: str ):
        if ord('a') <= ord(s) <= ord('z') or ord("0") <= ord(s) <= ord("9"):
            return True
        return False