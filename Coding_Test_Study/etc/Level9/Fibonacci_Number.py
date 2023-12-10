def Fibonacci(a,n1,n2):
    tmp = n2
    n2 += n1
    n1 = tmp
    a -= 1
    if a == 1 :
        return n2
    return Fibonacci(a,n1,n2)

if __name__ == "__main__" :
    a = int(input())
    if a == 0 : print(0)
    elif a == 1 : print(1)
    else : print(Fibonacci(a,0,1))