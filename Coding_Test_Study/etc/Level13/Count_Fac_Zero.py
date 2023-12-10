import math

a = int(input())
s = str(math.factorial(a))
cnt = 0
for i in range(len(s)-1,-1,-1):
    if s[i] == '0': cnt += 1
    else : break
print(cnt)