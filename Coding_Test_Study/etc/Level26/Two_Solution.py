import sys
input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int,input().split())))
s, e, S, Ans = 0, n-1, 0, 100000000000000
start, end = 0, 0
while(s < e):
    S = arr[s] + arr[e]
    if abs(S) < Ans:
        Ans = abs(S)
        start = s
        end = e
    if S == 0:
        print(arr[s], arr[e])
        exit()
    elif S < 0 :
        s += 1
    else:
        e -= 1
print(arr[start], arr[end])