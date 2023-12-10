import sys

a = list(map(int,sys.stdin.readline().split()))
b = {}
c = {}
d = ['-']*a[1]
# for i in range(a[0]):
#     b[i] = sys.stdin.readline().strip()
#     c[b[i]] = i
# for i in range(a[1]):
#     tmp = sys.stdin.readline().strip()
#     if tmp.isdigit() is True:
#         print(b[int(tmp)-1])
#     else:
#         print(c[tmp]+1)

for i in range(a[0]):
    tmp = sys.stdin.readline().strip()
    b[str(i + 1)] = tmp
    b[tmp] = str(i + 1)

for i in range(a[1]):
    tmp = sys.stdin.readline().strip()
    print(b[tmp])