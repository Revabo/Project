a = int(input())
b = cycle = 0
c = 100
temp = a
while(a != c) :
    b = (temp//10) + (temp%10)
    c = (temp%10)*10 + (b%10)
    temp = c
    cycle = cycle + 1
print(cycle)