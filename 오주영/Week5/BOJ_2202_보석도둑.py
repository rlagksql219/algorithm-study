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
변경사항: 힙 자료구조 적용 -> 통과
'''
