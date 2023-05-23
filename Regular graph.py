from collections import defaultdict

graph = defaultdict(list)

n, m = list(map(int, input().split()))

for _ in range(m):
    node1, node2 = list(map(int, input().split()))
    
    graph[node1].append(node2)
    graph[node2].append(node1)
    
initial = len(graph[1])
for i in range(2, n + 1):
    if len(graph[i]) != initial:
        print("NO")
        break
    
else:
    print("YES")
