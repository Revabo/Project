a = int(input())
n = [True]*10001
n[0] = n[1] = False
p = []
for i in range(10001):
    if n[i] == True:
        j = 2
        p.append(i)
        while i*j <= 10000:
            n[i*j] = False
            j += 1
for i in range(a):
    b = int(input())
    min = [0,0,b]
    '''for j in p:
        if j >= b : break
        for k in p:
            if j+k == b:
                if min[2] > k-j and k-j >= 0:
                    min[0] = j
                    min[1] = k
                    min[2] = k-j
                break
    print(min[0],min[1],sep=' ')'''
    
    half = b//2
    for j in range(half,1,-1):
        if j in p and b-j in p:
            print(j,b-j)
            break