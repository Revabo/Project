n = int(input())
a = list(map(int,input().split()))
o = list(map(int,input().split()))
max = -1000000001
result = 0
min = 1000000001

def Inter(x,result,o):
    global max
    global min
    if x == 0:
        result = a[0]
    if x == n-1:
        if max < result:
            max = result
        if min > result:
            min = result
        return
    
    if o[0] != 0:
        result += a[x+1]
        o[0] -= 1
        Inter(x+1,result,o)
        o[0] += 1
        result -= a[x+1]
    if o[1] != 0:
        result -= a[x+1]
        o[1] -= 1
        Inter(x+1,result,o)
        o[1] += 1
        result += a[x+1]
    if o[2] != 0:
        result *= a[x+1]
        o[2] -= 1
        Inter(x+1,result,o)
        o[2] += 1
        result //= a[x+1]
    if o[3] != 0:
        if result < 0:
            result = abs(result)
            result //= a[x+1]
            result = -(result)
        else:
            result //= a[x+1]
        o[3] -= 1
        Inter(x+1,result,o)
        o[3] += 1
    
        
Inter(0,0,o)
print(max,min,sep='\n')