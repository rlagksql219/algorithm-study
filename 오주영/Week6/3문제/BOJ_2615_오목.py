import sys

def find_c(list):
    for i,line in enumerate(list):
        # if line.find('11111') != line.find('22222'):    #둘 다 오목인 경우 제외 //이거도 필요 없었다.
            if line.find('11111')!=-1:
                if line.find('111111')==-1:         #육목 제외
                    return (1,i,line.find('11111'))
            if line.find('22222')!=-1:
                if line.find('222222')==-1:
                    return (2,i,line.find('22222'))
                
'''
# 25%에서 오답

# 문제점 발견 : 같은 라인에 6목과 5목이 동시에 있는 경우를 무시한다.
# 그런데 이 탐색방법이 안되면  문자열로 한 의미가 없다ㅠㅠ

# re 모듈을 활용해보자

인줄 알았는데 그냥 비겼을 때 0 출력을 못봐서 오답이었다. 삽질..
'''

field_hori=[sys.stdin.readline().rstrip().replace(' ','') for _ in range(19)]   #행 문자열
field_valt=list(map(''.join,zip(*field_hori)))  # 열 문자열
field_diag=[]   #대각 문자열

for j in range(19):
    diag1=diag2=diag3=diag4=''
    for i in range(19):
        if i+j<19:
            diag1+=field_hori[i][i+j]   #우하향 대각선, 1행 출발
            diag2+=field_hori[i+j][i]    #우하향 대각선, 1열 출발
            diag3+=field_hori[18-i][i+j]   #우상향 대각선, 19행 출발
            diag4+=field_hori[18-i-j][i]   #우상향 대각선, 1열 출발
            
    field_diag+=[diag1,diag2,diag3,diag4]
    
hori=find_c(field_hori)
valt=find_c(field_valt)
diag=find_c(field_diag)

if hori:
    print(hori[0])
    print(hori[1]+1,hori[2]+1)

elif valt:
    print(valt[0])
    print(valt[2]+1,valt[1]+1)
    
elif diag:
    print(diag[0])
    a=divmod(diag[1],4)
    if a[1]==0:         #나머지에 따라 [i][i+j] | [i+j][i] | [18-i][i+j] | [18-i-j][i]
        print(diag[2]+1,diag[2]+a[0]+1)
    if a[1]==1:
        print(diag[2]+a[0]+1,diag[2]+1)
    if a[1]==2:
        print(19-diag[2],diag[2]+a[0]+1)
    if a[1]==3:
        print(19-diag[2]-+a[0],diag[2]+1)
else: print(0)