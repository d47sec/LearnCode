#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    minV = arr[0]
    maxV = arr[0]
    total = 0 
    for i in arr:
        total += i 
        if i > maxV:
            maxV = i 
        if i < minV:
            minV = i 
    print(total-maxV, total - minV)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
