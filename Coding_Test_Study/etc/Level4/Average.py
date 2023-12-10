n = int(input())
a = list(range(0,n))
sum = 0
a = list(map(int,input().split()))
for i in range(n):
    sum = sum + a[i]/max(a)*100
print(sum/n)