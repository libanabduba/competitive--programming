from collections import defaultdict
n = input()

t = int(input())

graph = defaultdict(list)

for _ in range(t):
   var = list(map(int, input().split()))
   if len(var) == 3:
      graph[var[1]].append(var[2])
      graph[var[2]].append(var[1])

   else:
      print(*graph[var[1]])
