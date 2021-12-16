#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    list = []
    for i in grades:
        if i < 38:
            list.append(i)
        elif i % 5 == 0:
            list.append(i)
        else:
            temp = i % 10
            if temp > 5:
                temp = temp - 5
            temp2 = i + 5 - temp
            if temp2 - i < 3:
                i = temp2
                list.append(i)
            else:
                list.append(i)
    return list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
