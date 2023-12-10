import sys

a = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))
if a == 1:
    print(b[0]**2)
else:
    print(min(b)*max(b))