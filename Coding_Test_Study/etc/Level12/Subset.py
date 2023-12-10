import sys

a = sys.stdin.readline().strip()
s = set()
for i in range(len(a)):
    for j in range(i,len(a)):
        tmp = a[i:j+1]
        s.add(tmp)
print(len(s))