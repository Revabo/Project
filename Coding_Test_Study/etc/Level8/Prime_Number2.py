a = int(input())
b = int(input())
cnt = []
for i in range(a,b+1):
    for j in range(1,i):
        if i%j == 0 and j != 1: break
        elif j+1 == i: cnt.append(i)
if len(cnt) == 0 :
    print(-1)
    exit()
print(sum(cnt))
print(min(cnt))