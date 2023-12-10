a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
d = [0]*2
for i in range(2):
    if a[i] != b[i] and a[i] != c[i]: d[i] = a[i]
    elif a[i] == c[i]: d[i] = b[i]
    else : d[i] = c[i]
print(d[0],d[1],sep=' ')