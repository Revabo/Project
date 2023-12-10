import sys

a = list(str(sys.stdin.readline().strip()))
a.sort(reverse=True)
for i in range(len(a)):
    print(a[i],end='')