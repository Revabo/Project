import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(0)
    exit()
prime = []
arr = [False,False] + [True]*(n+1)

for i in range(2,n+1):
    if arr[i]:
        prime.append(i)
        for j in range(i*2,n+1,i):
            arr[j] = False
s, e = 0, 1
count, SUM = 0, prime[0]
while(s < len(prime)):
    if SUM >= n:
        if SUM == n : count += 1
        SUM -= prime[s]
        s += 1
    elif e == len(prime):
        SUM -= prime[s]
        s += 1
    else :
        SUM += prime[e]
        e += 1
print(count)