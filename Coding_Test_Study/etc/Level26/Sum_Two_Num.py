import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
m = int(input())
s, e = 0, n-1
count = 0
S = 0
while(s < e):
    S = arr[s] + arr[e]
    if S == m:
        count += 1
        s += 1
    elif S < m:
        s += 1
    else :
        e -= 1
print(count)