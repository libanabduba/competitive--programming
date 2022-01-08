class RecentCounter:

    def __init__(self):
        self.list = []

    def ping(self, t: int) -> int:
        self.list.append(t)
        while self.list[0] < t -3000:
            self.list.pop(0)
        return len(self.list)
