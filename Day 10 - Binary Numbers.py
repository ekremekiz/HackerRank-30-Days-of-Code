#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
   
    temp = 0
    boyut = 0
    
    while n > 0:
        binary = n % 2
        
        if binary == 1:
            temp +=1
            if temp > boyut:
                boyut = temp
            
        else:
            temp = 0
            
        n = n // 2
        
    print(boyut)
