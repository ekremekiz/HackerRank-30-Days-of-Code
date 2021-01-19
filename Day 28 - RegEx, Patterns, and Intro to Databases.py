#!/bin/python3

import math
import os
import random
import re
import sys

                            
if __name__ == '__main__':
    N = int(input())
    
    regex = re.compile("@gmail.com")
    
    firstNameList = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        
        if regex.search(emailID):
            firstNameList.append(firstName)
    
    firstNameList.sort()
    
    for i in firstNameList:
        print(i)
        
