a = int(input())
row = [0]*a
cnt = 0

def Check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def N_Queen(n):
    global cnt
    if n == a:
        cnt += 1
        return 
    for i in range(a):
        row[n] = i
        if Check(n):
            N_Queen(n+1)
                
N_Queen(0)
print(cnt)