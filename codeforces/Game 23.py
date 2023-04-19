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
   
    def myfunc(n,m):
        if m % n != 0:
            return -1
    
        memo = {}
    
        def backtrack(num, count):
            if num == m:
                return count
            
            if num > m:
                return -1
            
            if (num, count) in memo:
                return memo[(num, count)]
            
            result = max(backtrack(num * 2, count + 1), backtrack(num * 3, count + 1))
            memo[(num, count)] = result
            
            return result
    
        return backtrack(n, 0)
            
        
       
       
       
            
        
        
        
        
        
            
    # Main code
    # t = int(input())
   
    # for i in range(t):
    n, m = inlt()

    print(myfunc(n,m))
        

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()

   


