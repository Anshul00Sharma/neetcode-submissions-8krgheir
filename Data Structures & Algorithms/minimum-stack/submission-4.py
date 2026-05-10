class MinStack:

    def __init__(self):
        self.minStack = []
        self.lastIndex = -1
        self.stack = []

        

    def push(self, val: int) -> None:
        
        self.lastIndex += 1
        self.stack.append(val)
        if self.minStack:
            self.minStack.append(val if val < self.minStack[-1] else self.minStack[-1])
        else:
            self.minStack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        self.lastIndex -= 1

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]