n, m = map(int,input().split())
arr = list(map(int,input().split()))
max = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if max < arr[i]+arr[j]+arr[k] <= m:
                max = arr[i]+arr[j]+arr[k]
print(max)