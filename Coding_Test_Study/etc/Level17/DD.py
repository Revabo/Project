import sys

n, m = map(int,sys.stdin.readline().split())
s = list(map(int,sys.stdin.readline().split()))
r = [0 for i in range(1000000)]
mod = [0 for i in range(1001)]
count = 0

for i in range(n):
    r[i] = r[i-1] + s[i]
    mod[r[i] % m] += 1

for i in range(m):
    if mod[i] == 0 : continue
    count += mod[i] * (mod[i] - 1) // 2

print(count + mod[0])