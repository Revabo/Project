import itertools

n, m = map(int,input().split())
a = [ _ for _ in range(1,n+1)]
nPr = list(itertools.combinations_with_replacement(a,m))
for i in range(len(nPr)):
    for j in range(m):
        print(nPr[i][j],end=' ')
    print('')