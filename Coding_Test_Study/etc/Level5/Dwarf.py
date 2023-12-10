import sys

L = [0,0,0,0,0,0,0,0,0]
result = [0,0,0,0,0,0,0,0,0]

def Dwarf():
    for i in range(9):
        L[i] = int(sys.stdin.readline())
    Sum = sum(L)
    for i in range(9):
        for j in range(i+1,9):
            if (Sum - L[i] - L[j]) == 100:
                tmp1 = L[i]
                tmp2 = L[j]
                L.remove(tmp1)
                L.remove(tmp2)
                return L

if __name__ == '__main__':
    result = Dwarf()
    result.sort()
    for i in range(len(result)):
        print(result[i])