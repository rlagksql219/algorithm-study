import sys

L1,L2=[],[]
N=int(sys.stdin.readline())

for i in range(N):
    L1.append(sys.stdin.readline())
for i in range(N):
    L2.append(sys.stdin.readline())
    #append()와 insert(-1,)의 차이는?

ans=0
'''
for i in range(N):
    if L2.index(L1[i])<i:
        ans+=1
이 부분이 잘못되었다. 반례 : 1 2 3 4 5 | 2 1 5 4 3 
'''
for l in L2:
    if L1.index(l) != 0:
        ans+=1
        L1.remove(l)
    else: L1.remove(l)        

print(ans)

