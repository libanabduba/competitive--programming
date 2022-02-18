class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position,speed)]
        monstack = []
        for p,s in sorted(pair)[::-1]:
            monstack.append((target-p)/s)
            if len(monstack) >= 2 and monstack[-1] <= monstack[-2]:
                monstack.pop()
        return len(monstack)
