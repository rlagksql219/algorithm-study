import sys

input=sys.stdin.readline

N=int(input())
lt=list(map(int,input().split()))
order=[]
# order=[0 for i in range(N)]
# order[lt[0]]=1
for i in range(N,0,-1):
    order.insert(lt[i-1],i)

print(*order)
