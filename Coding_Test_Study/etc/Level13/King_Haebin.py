n = int(input())
for i in range(n):
    m = int(input())
    a = {}
    c = 1
    for j in range(m):
        tmp = list(map(str,input().split()))
        if tmp[1] in a:
            a[tmp[1]] += 1
        else:
            a[tmp[1]] = 1
    for key,value in a.items():
        c *= value+1
    print(c-1)