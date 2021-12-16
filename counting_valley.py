#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    sealevel = 0
    values = []
    count = 0
    for i in range(steps):
        if path[i] == "U":
            sealevel += 1
            values.append(sealevel)
        else:
            sealevel -= 1
            values.append(sealevel)
    for i in range(0, len(values)):
        if values[i] == 0 and values[i - 1] < 0:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
