#!/bin/python3

import math
import os
import random
import re
import sys


def MaxBitwise(n, k):
    temp = 0
    for i in range(1, n+1):
        for j in range(1, i):
            if (i&j > temp) and (i&j < k):
                temp = i&j
                if temp == k-1:
                    return temp
    return temp
    

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        
        liste=[]
        
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        print(MaxBitwise(n, k))
        
