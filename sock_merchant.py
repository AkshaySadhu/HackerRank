#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
        count = 0
        ar.sort()
        print(ar)
        for i in range(1, n):
            if (ar[i-1] == ar[i]):
                ar[i-1] = 0
                ar[i] = 0
        for i in range(n):
            if ar[i] > 0:
                count = count + 1
        return count
if __name__ == '__main__':
    
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
