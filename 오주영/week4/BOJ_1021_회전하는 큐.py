import sys

A1=list(map(int,sys.stdin.readline().split()))
A2=list(map(int,sys.stdin.readline().split()))
A=[A1,A2]
# print(A)

# A=[[32,6],[27,16,30,11,6,23]]
N=A[0][0]

q=[i+1 for i in range(N)]

ans=0

# print(q)

for i in range(A[0][1]):
    lt= q.index(A[1][i])
    # print(A[1][i],lt)
    if lt<N-lt:
        #왼쪽으로 회전
        q=q[lt:]+q[:lt]
        ans+=lt        
        # print(q, ans)
        q.pop(0)
        # print(q)
        
    else:
        #오른쪽으로 회전
        q=q[lt:]+q[:lt]
        ans+=N-lt
        # print(q, ans)
        q.pop(0)
        # print(q)
        
    N-=1
    

print(ans)
