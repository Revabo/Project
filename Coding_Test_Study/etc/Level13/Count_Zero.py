def Count(a,n):
    cnt = 0
    while a != 0:
        a = a // n
        cnt += a
    return cnt


n, m = map(int, input().split())

if m == 0:
    print(0)

else:
    print(min(Count(n,2) - Count(m,2) - Count(n - m,2), Count(n,5) - Count(m,5) - Count(n - m,5)))

