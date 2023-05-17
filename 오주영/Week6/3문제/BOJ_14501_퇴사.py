import sys

input=sys.stdin.readline

N=int(input())
gain=[0 for _ in range(N+1)]    
table=[tuple(map(int,input().split())) for _ in range(N)]

for d,l in enumerate(table):
    for i in range(d+l[0],N+1):
        if gain[i] < gain[d]+l[1]:
            gain[i] = gain[d]+l[1]
print(gain[-1])