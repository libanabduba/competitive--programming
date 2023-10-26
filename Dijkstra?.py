import heapq
from collections import defaultdict

def myfunc(n, graph):
    
   
    # Dijkstra's algorithm
    distance = [float('inf')] * n
    parent = [-1] * n
    distance[0] = 0
    heap = [(0, 0)]
    
    while heap:
        dist_u, u = heapq.heappop(heap)
        if dist_u > distance[u]:
            continue
        for v, w in graph[u]:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                parent[v] = u
                heapq.heappush(heap, (distance[v], v))
    
    # Reconstruct the shortest path
    if distance[n - 1] == float('inf'):
        print("-1")  # No path exists
    else:
        path = []
        v = n - 1
        while v != -1:
            path.append(v + 1)  # Convert back to 1-based indexing
            v = parent[v]
        path.reverse()
        print(*path)
        
        
        
  
# # Input
n, m = list(map(int, input().split()))
graph = defaultdict(list)

for _ in range(m):
    node1, node2, weight = list(map(int, input().split()))
   
    graph[node1 - 1].append([node2 - 1, weight])
    graph[node2 - 1].append([node1 - 1, weight])
    
myfunc(n, graph)
