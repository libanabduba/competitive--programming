#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    swapped = True
    count = 0
    while swapped:
        for i in range(len(a) - 1):
            if a[i] > a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
                count += 1
        
        for i in range(len(a) - 1):
            if a[i] < a[i+1]:
                swapped = False
            else:
                swapped = True
                break
    print(f"Array is sorted in {count} swaps." ) 
    print(f"First Element: {a[0]}") 
    print(f"Last Element: {a[-1]}")    
    return  
   
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
