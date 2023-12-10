a = int(input())
b = int(input())
c = int(input())
mul = a*b*c
mul = str(mul)
count = 0
for i in range(10):
    for j in range(len(mul)):
        if int(mul[j]) == i : count = count + 1
    print(count)
    count = 0
        