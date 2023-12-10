a = int(input())
for i in range(a):
    tmp = i
    for j in str(i):
        tmp += int(j)
    if tmp == a:
        print(i)
        exit()
print(0)