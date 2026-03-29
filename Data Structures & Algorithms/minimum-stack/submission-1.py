class MinStack:

    def __init__(self):
        self.lastIndex = -1
        self.arr = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.lastIndex += 1
        self.arr.append(val)
        if self.minstack:
            self.minstack.append(val if val < self.minstack[-1] else self.minstack[-1])
        else:
            self.minstack.append(val)

        

    def pop(self) -> None:
        self.lastIndex -= 1
        self.arr.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.arr[self.lastIndex]

        

    def getMin(self) -> int:
        return self.minstack[-1]
        
