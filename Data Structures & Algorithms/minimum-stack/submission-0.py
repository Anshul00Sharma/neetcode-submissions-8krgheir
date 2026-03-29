class MinStack:

    def __init__(self):
        self.lastIndex = -1
        self.arr = []
        

    def push(self, val: int) -> None:
        self.lastIndex += 1
        self.arr.append(val)
        

    def pop(self) -> None:
        self.lastIndex -= 1
        self.arr.pop()
        

    def top(self) -> int:
        return self.arr[self.lastIndex]

        

    def getMin(self) -> int:
        temp = [*self.arr]
        temp.sort()
        return temp[0]
        
