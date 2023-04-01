import math
import sys, threading
from collections import defaultdict, Counter
from sys import stdin, stdout
 
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
 
 
def inp():
    return int(stdin.readline())
 
 
def inlt():
    return list(map(int, stdin.readline().strip().split()))
 
 
def insr():
    s = stdin.readline().strip()
    return list(s[:len(s)])
 
 
def invr():
    return map(int, stdin.readline().strip().split())
 
def main():
   
    def myfunc(n,arr):
        
        if n == 1:
            print(1)
            print(1)
            print(1)
            
            return
        
        def dfs(node):
            
            if node in visited:
                return []
            
            visited.add(node)
            
            if node == dic[node]:
                return [node]
                
            e = dfs(dic[node])
            
            
            
            e.append(node)
        
            return e
            
        
        dic = {}
        not_leaf = set(arr)
    
        for i in range(n):
            dic[i+1] = arr[i]
            
            
        leaf = []
        
        for i in range(1,n+1):
            if i not in not_leaf:
                leaf.append(i)
        ans = []
        visited = set()
        
        for val in leaf:
            # print("hello")
            ans.append(dfs(val))
            
            
        print(len(ans))
        
        # print(ans)
        
        for i in ans:
            print(len(i))
            print(*i)
        
        # print()
            
            
            
                
        
                
            
            
            
    # Main code
    t = int(input())
    
    for i in range(t):
        n = inp()
        arr = inlt()
        myfunc(n,arr)
        print()
 
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
