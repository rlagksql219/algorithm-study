N=int(input())
rest5=N%5
q5=N//5
if rest5:
    if rest5==3: print(q5+1)
    elif N>5:
        if rest5==1: print(q5+1)
        elif rest5==4: print(q5+2)
        elif N>10 and rest5==2: print(q5+2)    
        else: print(-1)
    else: print(-1)
else: print(q5)


# #while문을 활용한 경우
N = int(input())
a = 0
while N >= 0:
    if N % 5 == 0:
        a += (N//5)
        print(a)
        break
    N = N - 3
    a = a + 1
else:
    print(-1)
    

#인상깂었던 코드
N = int(input())
print([N//5+[0,1,2,1,2][N%5],-1][N in [4,7]])
