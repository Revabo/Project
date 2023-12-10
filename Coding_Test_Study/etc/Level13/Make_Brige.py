import math

n = int(input())
for i in range(n):
    a = list(map(int,input().split()))
    print(math.factorial(a[1])//(math.factorial(a[1]-a[0])*math.factorial(a[0])))