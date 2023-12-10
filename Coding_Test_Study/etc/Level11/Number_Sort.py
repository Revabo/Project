import sys

a = int(input())
b = [0]*10000
for i in range(a):
    tmp = int(sys.stdin.readline())
    b[tmp-1] += 1
for i in range(10000):
    if b[i] != 0:
        for j in range(b[i]):
            print(i+1)