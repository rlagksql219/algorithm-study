import sys

input=sys.stdin.readline

rc=list(map(int,input().split()))

field=[input().strip() for i in range(rc[0])]
fstr=''
for i in field:
    fstr+=i    
home=divmod(fstr.find('D'),rc[1])
start=divmod(fstr.find('S'),rc[1])    
    
def findAll(str,a)->list:   #a의 모든 초기 위치의 리스트를 반환
    num_a=str.count(a)
    if num_a!=-1:
        init_a=[fstr.find(a) for i in range(num_a)]
        return init_a
  

def cordAll(a=list,Col=int)->list:
    return [divmod(i,Col) for i in a]

def adj(dict,tuple,t):
    u=(tuple[0],tuple[1]+1)
    d=(tuple[0],tuple[1]-1)
    r=(tuple[0]+1,tuple[1])
    l=(tuple[0]-1,tuple[1])
    
    case=list(filter(lambda i: dict.get(i,[100])[0]=='.' or dict.get(i,[100])[0]=='S',[u,d,r,l]))
   
    # print('case',case,t)
    
    for i in case:    
        dict[i]=('*',t+1)      #어차피 field를 따로 쓰기 때문에 되돌아가기 방지로 값도 변경.
        # print(i,dict[i],t)

        if t<=dict[i][1]:
            adj(dict,i,t+1)
    # print(dict)
            
def ust(dict,tuple,t):
    u=(tuple[0],tuple[1]+1)
    d=(tuple[0],tuple[1]-1)
    r=(tuple[0]+1,tuple[1])
    l=(tuple[0]-1,tuple[1])
    
    case=list(filter(lambda i: dict.get(i,[100])[0]=='.' or dict.get(i,[100])[0]=='D',[u,d,r,l]))
   
    # print('case',case)
    
    for i in case:    
        dict[i]=('S',t+1)      #어차피 field를 따로 쓰기 때문에 되돌아가기 방지로 값도 변경.
        print(i,dict[i],t)
    for i in case:
        if t<=dict[i][1]:
            adj(dict,i,t+1)
    



pw=findAll(fstr,'*')
cord_pw=cordAll(pw,rc[1])  
cart={divmod(i,rc[1]):[fstr[i],0] for i in range(rc[0]*rc[1])} 
cart_w={}
for i in cord_pw:
    cart_w[i]={divmod(i,rc[1]):[fstr[i],0] for i in range(rc[0]*rc[1])}
for cord in cord_pw:
    adj(cart_w[i],cord,0)
# adj
print(cart_w)
