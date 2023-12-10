import sys

b = []
index = 0

a = int(sys.stdin.readline())
for i in range(a):
    tmp = input()
    b.append(tmp)
    if tmp == 'ENTER':
        b = set(b)
        index += len(b) - 1
        b = []
b = set(b)
index += len(b)
print(index)