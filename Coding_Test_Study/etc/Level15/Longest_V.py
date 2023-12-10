import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
b = [1]*n
c = [1]*n
for i in range(1,n):
    for j in range(i):
        if a[j] < a[i]:
            tmp = b[j] + 1
            if tmp > b[i] :
                b[i] = tmp
        elif a[j] > a[i]:
            tmp1 = c[j] + 1
            tmp2 = b[j] + 1
            if tmp1 > c[i] or tmp2 > c[i]:
                c[i] = max(tmp1,tmp2)
print(max(max(b),max(c)))