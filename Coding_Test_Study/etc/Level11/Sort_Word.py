import sys

a = int(sys.stdin.readline())
b = []
for i in range(a):
    tmp = str(sys.stdin.readline().strip())
    if tmp in b:
        continue
    b.append(tmp)
b.sort(key = lambda x : (len(x), x))
for i in range(len(b)):
    print(b[i])