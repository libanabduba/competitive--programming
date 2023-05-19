from collections import defaultdict

graph = defaultdict(list)

n = int(input())

for i in range(n):
   row = list(map(int, input().split()))
   for j in range(n):
      if row[j] == 1:
         graph[i+1].append(j + 1)

for key, value in graph.items():
   print(len(value), *(value))
