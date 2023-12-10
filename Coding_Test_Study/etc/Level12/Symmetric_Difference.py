import sys

n = list(map(int,sys.stdin.readline().split()))
a = set(map(int,sys.stdin.readline().split()))
b = set(map(int,sys.stdin.readline().split()))
a1 = a - b
b1 = b - a
print(len(a1)+len(b1))