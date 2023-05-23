from collections import defaultdict

graph = {}




n = int(input())

for node in range(n):
    graph[node + 1] = [0,0]

for i in range(n):
    row = list(map(int, input().split()))
    
    for j in range(len(row)):
        if row[j] == 1:
            graph[i + 1][1] += 1
            graph[j + 1][0] += 1
            
# print(graph)

sources = []
sinks = []
           
for node in graph:
    if graph[node][0] == 0:
        sources.append(node)
    if graph[node][1] == 0:
        sinks.append(node) 
        

print(len(sources), *sources) 
print(len(sinks), *sinks)
