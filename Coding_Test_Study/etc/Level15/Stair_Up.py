import sys

a = int(sys.stdin.readline())
b = [0 for i in range(a)]
for i in range(a):
    b[i] = int(sys.stdin.readline())
m = [0 for i in range(a)]

if a == 1:
    print(b[0])
    exit()
elif a == 2:
    print(b[0]+b[1])
    exit()
    
m[0] = b[0]
m[1] = b[1] + b[0]
m[2] = b[2] + max(b[0],b[1])
def Climb(n):
    if n == a:
        return
    tmp0 = b[n] + b[n-1] + m[n-3]
    tmp1 = b[n] + m[n-2]
    m[n] = max(tmp0,tmp1)
    Climb(n+1)
Climb(3)
print(m[a-1])