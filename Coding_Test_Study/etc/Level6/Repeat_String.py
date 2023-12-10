a = int(input())
for i in range(a):
    b, s = input().split(' ')
    for j in range(len(s)):
        print(s[j]*int(b),end='')
    print('')