import math

T = int(input())
for i in range(T):
    n = int(input())
    prime = True
    
    if n <= 1:
        prime = False
    
    sqrt_n = math.sqrt(n)
    if sqrt_n.is_integer == True:
        prime = False
    for j in range(2,int(sqrt_n)+1):
        if n%j == 0:
            prime = False
    
    if prime == True:
        print("Prime")
    else:
        print("Not prime")