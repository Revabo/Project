import sys
input = sys.stdin.readline

N, S = map(int,input().split())
arr = list(map(int,input().split()))
s, e = 0, 1
length, SUM = 10000000, arr[0]
while(s < N):
    if SUM >= S:
        length = min(length, e-s)
        SUM -= arr[s]
        s += 1
    elif e == N:
        SUM -= arr[s]
        s += 1
    else :
        SUM += arr[e]
        e += 1
if length == 10000000:
    print(0)
else:
    print(length)