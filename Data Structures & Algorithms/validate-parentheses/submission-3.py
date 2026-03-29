class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack.append(s[0])

        for i in range(1,len(s)):
            if s[i] in maps and stack and maps[s[i]] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        
        return False if (len(stack) > 0) else True