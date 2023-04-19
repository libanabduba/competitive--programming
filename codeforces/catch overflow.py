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
   
    def myfunc(f):
        x = 0
        stack = []
        for line in f:
            
            line = line.split()
            if len(line) == 2:
                stack.append([int(line[1]), 0])
            else:
                if line[0] == "add":
                    if stack:
                        stack[-1][1] += 1
                    else:
                        x += 1
                else:
                    n, val = stack.pop()
                    if stack:
                        stack[-1][1] += n * val
                    else:
                        x += n * val
        
        if x < 2**32:
            print(x)
        else:
            print("OVERFLOW!!!")
                
        
        
        
        
            
    # Main code
    # t = int(input())
    # maxi = float("-inf")
    # for i in range(t):
    # n, time = list(map(int, input().split()))
    n = inp()
    arr = []
    for _ in range(n):
       arr.append(input())
    myfunc(arr)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
