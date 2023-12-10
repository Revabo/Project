a = int(input())
for i in range(a):
    count = 0
    n = list(map(int,input().split()))
    average = (sum(n) - n[0]) / n[0]
    for j in range(n[0]):
        if n[j+1] > average : count = count + 1
    print('{:.3f}%'.format(round(count/n[0]*100,3)))