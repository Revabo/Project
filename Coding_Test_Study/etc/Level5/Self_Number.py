def Self_Num :
    for i in range(10000):
    for j in range((len(str(i)))*9):
        tmp = i - j
        if i < 10 :
            if i == tmp + tmp%10 : break
            elif j+1 == (len(str(i)))*9 : print(i)
        elif i < 100 :
            if i == tmp + tmp//10 + tmp%10 : break
            elif j+1 == (len(str(i)))*9 : print(i)
        elif i < 1000 :
            if i == tmp + tmp//100 + (tmp//10)%10 + tmp%10 : break
            elif j+1 == (len(str(i)))*9 : print(i)
        elif i < 10000 :
            if i == tmp + tmp//1000 + (tmp//100)%10 + (tmp//10)%10 + tmp%10 : break
            elif j+1 == (len(str(i)))*9 : print(i)
                
if __name__ == "__main__":
    Self_Num()