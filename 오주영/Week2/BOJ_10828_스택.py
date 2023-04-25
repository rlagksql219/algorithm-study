import sys  #입력을 stdin 형태로 받기 위해 불러온다.


S = []

#Steak 기능 구현 ~ list를 이용해서
def push(S : list, any):    #레퍼런스에서는 any 대신 f, f[1]을 사용했다. 장점이 있나?
    d = int(any)
    S.append(d)             #데이터를 가장 오른쪽에 넣는다.

def pop(S):
    if S == []:
        print(-1)
    else:
        value = S[len(S)-1] #S의 가장 오른쪽 값이다 /레퍼런스 때문에 직접 print를 씌우지 않았는데 이유가 궁금하다(아마도 활용을 위해?)
        S.pop()             #S에서 가장 오른쪽 값을 지운다
        print(value)

def top(S):
    if S == []:
        print(-1)
    else:
        print(S[len(S)-1])

def empty(S):
    if S==[]:
        print(1)
    else:
        print(0)

def size(S):
    print(len(S))




N = int(sys.stdin.readline()) #문자열을 int로 형변환 하면 개행문자 지워짐

for i in range(N):
    f = sys.stdin.readline().split() #문자열을 공백단위로 / f[0]이 명령어가 된다

    if f[0]=='push':
        push(S,f[1])
    elif f[0]=='pop':
        pop(S)
    elif f[0]=='top':
        top(S)
    elif f[0]=='empty':
        empty(S)
    elif f[0]=='size':
        size(S)
    
    '''함수명과 f[0]가 같은데 코드를 더 짧게 하는 방법이 있을까?'''
