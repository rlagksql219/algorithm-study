import sys

R=['M','D','C','L','X','V','I','CM','CD','XC','XL','IX','IV'] #단일문자의 갯수를 먼저 세어 더하고
D=[1000,500,100,50,10,5,1,-200,-200,-20,-20,-2,-2]            #CM 등 역순 등장의 경우에 두배로 빼준다.
A=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
E=[1000,900,500,400,100,90,50,40,10,9,5,4,1]

a,b= sys.stdin.read().splitlines()

def dec(rome):
    N=0
    for i in range(len(R)):
        el=rome.count(R[i])
        if el != 0:
            N+=el*D[i]
    return N
  
  
def rome(N):
    Rm=str()
    for k in range(len(A)):
        Rm+=A[k]*(N//E[k]) 
        N=N%E[k]
    return Rm
    

print(dec(a)+dec(b))
print(rome(dec(a)+dec(b)))
