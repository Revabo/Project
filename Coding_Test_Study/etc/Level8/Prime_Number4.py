'''import math

a = 1
n = [1]*(246913)
while True :
    a = int(input())
    if a == 0 : break
    b = a*2
    n[0] = n[1] = 0
    for i in range(2,b+1):
        if n[i] == 1:
            j = 2
            while i*j <= b:
                n[i*j] = 0
                j += 1
    print(sum(n[a+1:b+1]))'''