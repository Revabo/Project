import sys

k = int(sys.stdin.readline())
stack = []

def Zero():
    for i in range(k):
        com = int(sys.stdin.readline())
        if com != 0:
            stack.append(com)
        else:
            stack.pop()
    return sum(stack)
    
if __name__ == '__main__':
    print(Zero())