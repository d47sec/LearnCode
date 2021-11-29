#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    hashMap = {"positive":0, "negative":0, "zero":0}
    for val in arr:
        if val > 0:
            hashMap["positive"] += 1
        elif val < 0:
            hashMap["negative"] += 1
        else:
            hashMap["zero"] += 1
    print(round((hashMap["positive"]/len(arr)),6)) 
    print(round((hashMap["negative"]/len(arr)),6))
    print(round((hashMap["zero"]/len(arr)),6))
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
    


# NOTE: SỬ DỤNG HÀM ROUND TRONG PYTHON ĐỂ LẤY SỐ CHỮ SỐ THẬP PHÂN TRONG PYTHON 