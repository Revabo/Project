import sys

def fac(a):
    if a == 0 : return 1
    return a * fac(a-1)

a = int(sys.stdin.readline())
print(fac(a))