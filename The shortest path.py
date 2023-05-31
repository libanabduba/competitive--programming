from collections import defaultdict,deque

graph = defaultdict(set)

n, m = list(map(int, input().split()))

a, b = list(map(int, input().split()))

if a == b:
    return -1

for _ in range(m):
    
    node1, node2 = list(map(int, input().split()))
    graph[node1].add(node2)
    graph[node2].add(node1)
    
# print(graph)
q = deque([(a, 0, [a])])

visited = set([a])


def bfs():

    while q:
        
        node, path_count, path = q.popleft()
        # print(node, path)
        
        if node == b:
            return (path_count, path)
        
        for neigh in graph[node]:
            # print(path)
            
            if neigh not in visited:
                visited.add(neigh)
                copy_path = path[::]
                copy_path.append(neigh)
                q.append((neigh, path_count + 1, copy_path))
                
                
    return -1


value = bfs()

if value == -1: print(value)
else:
    print(value[0])
    print(*(value[1]))
