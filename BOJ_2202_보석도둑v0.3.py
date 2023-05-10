import sys
import heapq
input=sys.stdin.readline

N,K=map(int,input().split())
catalog=list()
for i in range(N):
    heapq.heappush(catalog, tuple(map(int,input().split())))
pocket=sorted(list(int(input()) for i in range(K)))

ans=0

hand=[]
for c in pocket:
    while catalog and c>= catalog[0][0]:
        heapq.heappush(hand, -heapq.heappop(catalog)[1])
    if hand:
        ans-= heapq.heappop(hand)
    elif not catalog:
        break


print(ans)
'''
변경사항: 무게당 가격기준이 아닌 가격 기준으로 변경(나누기, 곱하기, int() 횟수 감소)
시간초과
'''