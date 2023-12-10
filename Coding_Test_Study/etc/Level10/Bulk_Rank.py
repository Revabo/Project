a = int(input())
n = [[a,a,a] for _ in range(a)]
for i in range(a):
    n[i][0], n[i][1] = map(int,input().split())
for i in range(len(n)):
    for j in range(len(n)):
        if n[i][0] >= n[j][0] or n[i][1] >= n[j][1]:
            if i != j:
                n[i][2] -= 1
for i in range(len(n)):
    print(n[i][2],end=' ')
print('')