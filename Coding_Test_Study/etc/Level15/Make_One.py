import sys

a = int(sys.stdin.readline())
b = [999999]*1000001
for i in range(a+1):
    tmp0 = tmp1 = tmp2 = 0
    if i == 0: continue
    elif i == 1:
        b[i] = 0
        continue
    if i%3 == 0:
        tmp0 = i//3
    if i%2 == 0:
        tmp1 = i//2
    tmp2 = i-1
    b[i] = min(b[tmp0],b[tmp1],b[tmp2]) + 1
print(b[a])