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
   
    def myfunc(n,D,arr):
        
        arr.sort(reverse=True)
        ans = 0
        total_power = 0
        temp_list = []
        for val in arr:
            temp_list.append(math.ceil((D+1)/val))
            
        for val in temp_list:
            total_power += val
            if total_power <= n:
                ans += 1
        return ans
       
       
            
        
        
        
        
        
            
    # Main code
    # t = int(input())
   
    # for i in range(t):
    n, D = inlt()
 
    # for i in range(n):
    arr = inlt()
    print(myfunc(n,D,arr))
        
 
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
