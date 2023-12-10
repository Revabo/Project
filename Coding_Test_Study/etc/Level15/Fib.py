cnt1 = cnt2 = 0
f = []

def fib(n):
    global cnt1
    if n == 1 or n == 2:
        cnt1 += 1
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fibonacci(n):
    global cnt2
    f.append(1) 
    f.append(1)
    for i in range(2,n):
        cnt2 += 1
        f.append(f[i-1] + f[i-2])
    return f[n-1]

a = int(input())
fib(a)
fibonacci(a)
print(cnt1, cnt2, sep=' ')