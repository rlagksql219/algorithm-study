import sys  #입력을 stdin 형태로 받기 위해 불러온다.


S = []

#queue 기능 구현 ~ list를 이용해서 
def push(S : list, any):    
    # d = int(any)     #생각해보니 int를 쓸 이유가?
    S.insert(0,any)    #제일 왼쪽에 넣는다 ; 이러면 stack의 뼈대를 재활용할 수 있다.     

def pop(S):
    if S == []:
        print(-1)
    else:
        value = S[len(S)-1] #S의 가장 오른쪽 값이다 
        S.pop()             #S에서 가장 오른쪽 값을 지운다
        print(value)

def front(S):
    if S == []:
        print(-1)
    else:
        print(S[-1])        #음수 인덱스는 -1부터 오른쪽에서 왼쪽

def back(S):
    if S == []:
        print(-1)
    else:
        print(S[0])

def empty(S):
    if S==[]:
        print(1)
    else:
        print(0)

def size(S):
    print(len(S))




N = int(sys.stdin.readline()) #문자열을 int로 형변환 하면 개행문자 지워짐

for i in range(N):
    f = sys.stdin.readline().split() #문자열을 공백단위로 / f[0]이 시동어가 된다

    if f[0]=='push':
        push(S,f[1])
    elif f[0]=='pop':
        pop(S)
    elif f[0]=='front':
        front(S)
    elif f[0]=='back':
        back(S)
    elif f[0]=='empty':
        empty(S)
    elif f[0]=='size':
        size(S)
    
    '''함수명과 f[0]가 같은데 코드를 더 짧게 하는 방법이 있을까?'''
