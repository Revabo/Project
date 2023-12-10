t = int(input())
for i in range(t) :
    k = int(input())
    n = int(input())
    a = [[x for x in range(1,n+1) ] for y in range(k+1)]
    for j in range(1,n):
        for l in range(k):
            a[l][j] = a[l-1][j] + a[l][j-1]
    print(max(max(a)))