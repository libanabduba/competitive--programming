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
        
        left = 0
        right = (4 * n) - 1
        
 
        arr.sort()
        
        area = arr[left] * arr[right]
        
        # print(arr)
        
        while left < right:
            
            if arr[left] == arr[left + 1] and arr[right] == arr[right - 1] and (arr[left] * arr[right]) == area:
                area = arr[left] * arr[right]
                left += 2
                right -= 2
                continue
        
            return "NO"
                
        return "YES"
        
        
            
            
       
       
            
    # Main code
    t = inp()
    
    for _ in range(t):
        n = inp()
        arr = inlt()
        print(myfunc(n, arr))
    # print(maxi)
 
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
