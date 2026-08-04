class MinStack:
    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        if len(self.arr) == 0:
            self.arr.append((val, val))
            return
        temp = self.arr[-1]
        min_value = temp[1]

        if val < min_value:
            self.arr.append((val, val))
        else:
            self.arr.append((val, temp[1]))

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:
        return self.arr[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
