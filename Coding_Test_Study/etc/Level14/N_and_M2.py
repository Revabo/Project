import itertools

n, m = map(int,input().split())
a = [ _ for _ in range(1,n+1)]
nCr = itertools.combinations(a,m)
nCr = list(nCr)
for i in range(len(nCr)):
    for j in range(m):
        print(nCr[i][j],end=' ')
    print('')