a = int(input())
if a == 1: exit()
i = 2
while i <= a:
    if a%i == 0 :
        print(i)
        a /= i
    else :
        i += 1