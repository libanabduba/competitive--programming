from collections import defaultdict

graph = defaultdict(list)

n = int(input())
ans = []
for _ in range(n):
    row = list(map(int, input().split()))
    temp = [0] * n
    if len(row) > 1:
        for j in range(1,len(row)):
            temp[row[j] - 1] = 1
        
    ans.append(temp[::])
    
for val in ans:
    print(*(val))
