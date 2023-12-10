s = input()
for i in range(97,123):
    for j in range(len(s)):
        if i == ord(s[j]) : 
            print(j, end=' ')
            break
        elif j+1 == len(s) : print(-1, end=' ')