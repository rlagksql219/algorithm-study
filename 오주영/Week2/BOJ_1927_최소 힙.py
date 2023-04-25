# import sys
# sys.setrecursionlimit(10**7) #RecursionError: maximum recursion depth exceeded in comparison를 막기 위해 최대재귀를 설정해봤다.

# def min(H):
#     H=list(set(H))
#     print(min(H))
#     H.remove(min(H))
# H=[]
# # N=list(map(int,sys.stdin.readline()))
# N=list(map(int,input().split()))
# for i in N:
#     H.append(i)
#     if i == 0:
#         if H==[]:
#             print(0)
#         else:
#             min(H)
# '''이렇게 접근했더니 런타임이 너무너무 오래 걸린다'''

from heapq import heappush, heappop #내장 모듈이다

H=[]

N = list(map(int,input().split()))


for i in N:
    a=int(i)
    if i!=0:
        heappush(H,i)
    else:
        if H==[]:
            print(0)
        else:
            print(heappop(H))

# '''왜 틀리는지 모르겠어요..'''
