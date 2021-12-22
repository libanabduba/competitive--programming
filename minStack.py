class MinStack:

    def __init__(self):
        
        self.stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        min = self.stack[0]
        for i in range(len(self.stack)):
            if self.stack[i] < min:
                min = self.stack[i]
        return min
