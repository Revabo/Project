n, m = map(int,input().split())
a = [['A' for _ in range(m)] for _ in range(n)]
chess1 = ['B','W','B','W','B','W','B','W']
chess2 = ['W','B','W','B','W','B','W','B']
min = 64
for i in range(n):
    a[i] = list(input())
for i in range(n-7):
    for j in range(m-7):
        cnt1 = cnt2 = 0
        for k in range(8):
            for l in range(8):
                if k%2 == 0:
                    if chess1[l] != a[i+k][j+l]:
                        cnt1 += 1
                    if chess2[l] != a[i+k][j+l]:
                        cnt2 += 1
                else:
                    if chess2[l] != a[i+k][j+l]:
                        cnt1 += 1
                    if chess1[l] != a[i+k][j+l]:
                        cnt2 += 1
        if min > cnt1 :
            min = cnt1
        if min > cnt2 :
            min = cnt2
print(min)