a = list()
remain = list()
count = 0
for i in range(10):
    a.append(int(input()))
    remain.append(a[i] % 42)
    if remain.count(remain[i]) == 1 : 
        count = count + 1
print(count)