a, b = map(int,input().split())
n = [True]*(b+1)
n[0]= n[1] = False
for i in range(2,b+1):
    j = 2
    while i*j <= b:
        n[i*j] = False
        j += 1
for i in range(a,len(n)):
    if n[i] == True:
        print(i)