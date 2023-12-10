import sys
import math

a = list(map(int,sys.stdin.readline().split()))
for i in range(a[0]):
    tmp = int(sys.stdin.readline().strip())
    if tmp <= ((a[1]**2)+(a[2]**2))**(1/2): print('DA')
    else: print('NE')