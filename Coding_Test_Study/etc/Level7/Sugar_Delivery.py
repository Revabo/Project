a = int(input())
n = []
if a%5 == 0 : n.append(a//5)
if a%3 == 0 : n.append(a//3)
for i in range(1,(a//5)+1):
    for j in range(1,(a//3)+1):
        if (i*5)+(j*3) == a : n.append(i+j)
print(min(n) if len(n) != 0 else -1)