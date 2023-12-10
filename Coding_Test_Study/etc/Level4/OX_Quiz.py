n = int(input())
a = list()
score = count = 0
for i in range(n):
    a.append(input())
    for j in range(len(a[i])):
        if a[i][j] == 'O':
            count = count + 1
            score = score + count
        elif a[i][j] == 'X':
            count = 0
    print(score)
    score = count = 0