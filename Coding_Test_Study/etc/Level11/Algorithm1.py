import sys

def Check(a,b,c,n):
    if a*n+b <= c*n and c >= a:
        return 1
    else : return 0


a,b = map(int,sys.stdin.readline().split())
c = int(sys.stdin.readline())
n = int(sys.stdin.readline())
print(Check(a,b,c,n))