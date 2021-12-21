class MyQueue:

    def __init__(self):
        self.list = []

    def push(self, x: int) -> None:
        self.list.append(x)
    def pop(self) -> int:
        return self.list.pop(0)
    def peek(self) -> int:
        return self.list[0]

    def empty(self) -> bool:
        if len(self.list) == 0:
            return True
        return False
