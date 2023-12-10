import sys

a = list(map(int,sys.stdin.readline().split()))
b = {}
cnt = 0
for i in range(a[0]):
    tmp = sys.stdin.readline().strip()
    b[tmp] = 1
for i in range(a[1]):
    tmp = sys.stdin.readline().strip()
    if tmp in b:
        b[tmp] = 2
        cnt += 1
    else:
        b[tmp] = 1
b = dict(sorted(b.items()))
print(cnt)
for key, value in b.items():
    if value == 2:
        print(key)