class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-*/"

        for element in tokens:
            if element not in operators:
                stack.append(int(element))
            elif element == '+':
                a2 = stack.pop()
                a1 = stack.pop()
                stack.append(a1+a2)
            elif element == '-':
                a2 = stack.pop()
                a1 = stack.pop()
                stack.append(a1-a2)
            elif element == '*':
                a2 = stack.pop()
                a1 = stack.pop()
                stack.append(a1*a2)
            elif element == '/':
                a2 = stack.pop()
                a1 = stack.pop()
                stack.append(int(a1/a2))
        return stack.pop()