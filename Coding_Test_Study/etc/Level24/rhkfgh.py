import sys

k = int(sys.stdin.readline())

for i in range(k):
    tmp = input()
    stack = []
    for j in range(len(tmp)):
        if tmp[i] == '(':
            stack.append(tmp[i])
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')