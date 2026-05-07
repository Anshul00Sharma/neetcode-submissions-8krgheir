class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for c in s:
            if c in maps:
                if stack and stack[-1] == maps[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return False if len(stack) > 0 else True  



        