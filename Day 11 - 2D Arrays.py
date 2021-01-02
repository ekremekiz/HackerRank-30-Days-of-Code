#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    max_kum_saati = -63
    for satir in range(1,5,1):
        for sutun in range(1,5,1):
            if satir <= 5 and sutun <= 5:
                ust = arr[satir-1][sutun-1]+arr[satir-1][sutun]+arr[satir-1][sutun+1]
                orta = arr[satir][sutun]
                alt = arr[satir+1][sutun-1]+arr[satir+1][sutun]+arr[satir+1][sutun+1]
                toplam = ust + orta + alt
                if (toplam>max_kum_saati):
                    max_kum_saati = toplam

    print(max_kum_saati)
