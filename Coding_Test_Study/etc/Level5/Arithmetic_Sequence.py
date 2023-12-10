def Arith_Seq(n) :
    count = 0
    for i in range(1,n+1):
        tmp = list(map(int,str(i+1)))
        if i < 100 : count = count + 1
        elif i//100+i%10 == i//10%10*2 : count = count + 1
#        elif i+1 < 1000 :
#            if (tmp[0] - tmp[1]) == (tmp[1] - tmp[2]) : count = count + 1
#        else :
#            if (tmp[0] - tmp[1]) == (tmp[1] - tmp[2]) == (tmp[2] - tmp[3]) : count = count + 1
    print(count)
    
if __name__ == "__main__" :
    Arith_Seq(int(input()))