a = cnt = int(input())
n = list(map(int,input().split()))
for i in range(a) :
    for j in range(2,n[i]):
        if n[i]%j == 0 or n[i] == 1: 
            cnt -= 1
            break
print(cnt)