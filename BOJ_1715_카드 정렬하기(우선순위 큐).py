import sys
from queue import PriorityQueue
input=sys.stdin.readline

N=int(input())
que = PriorityQueue()
for i in range(N):
    que.put(int(input()))
ans=0
for i in range(N-1):
    dec=que.get()+que.get()
    ans+=dec
    que.put(dec)
print(ans) 

'''
 내부적으로 heap 모듈을 사용하는 PriorityQueue 클래스의
 put(), get() 함수는 O(log n)의 시간 복잡도를 가진다.

 공부해볼 코드:
 from heapq import*
n,*c=map(int,open(0))
heapify(c)
print(sum(heappush(c,x:=heappop(c)+heappop(c))or x for _ in c[1:])
 
from heapq import*
p=heappop
n,*h=map(int,open(0));h.sort()
print(sum(heappush(h,t:=p(h)+p(h)) or t for _ in h[1:]))
 '''