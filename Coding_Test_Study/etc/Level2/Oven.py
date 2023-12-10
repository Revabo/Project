A, B = map(int,input().split())
C = int(input())
# print((A+int((B+C)/60))%24, (B+C)%60)
# print((h+m//60)%24,m%60)
B = B + C
if(B > 60):
    A = A + (B // 60)
    if(A >= 24):
        A = A % 24
    B = B % 60
print(A, B)