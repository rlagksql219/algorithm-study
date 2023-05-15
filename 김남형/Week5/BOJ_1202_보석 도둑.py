import sys
import heapq

input = sys.stdin.readline

jewel = []
bags = []
tmp_jewel = []
answer = 0

n, k = map(int, input().split())

for _ in range(n):
    heapq.heappush(jewel, list(map(int, input().split()))) # 최소 힘으로 정렬

for _ in range(k):
    bags.append(int(input()))

bags.sort()

for bag in bags:
    while jewel and bag >= jewel[0][0]: # 가방의 최대 수용 무게보다 최소 값(가장 가벼운 보석의 무게)이 작다면
        heapq.heappush(tmp_jewel, -heapq.heappop(jewel)[1]) # 보석 값을 최대 힙으로 정렬 (값의 부호 변경)
    if tmp_jewel:
        answer -= heapq.heappop(tmp_jewel) # 최대 값(가장 비싼 보석의 값)을 더한다
    elif not jewel:
        break
print(answer)

# 작은 가방부터 담을 수 있는 최대한의 비싼 보석을 챙겨가면 된다. 
# 힙을 사용해 시간 초과 해결

# 첫 풀이 (시간 초과)

# import sys

# input = sys.stdin.readline

# bag = []
# sum = 0

# n, k = map(int, input().split())

# jewel = [tuple(map(int, input().split())) for _ in range(n)]

# for _ in range(k):
#     bag.append(int(input()))

# jewel.sort(key = lambda x:(-x[1], x[0])) # 비싼 순서대로 정렬하고, 값이 같은 경우 가벼운 순서대로 정렬
# bag.sort() # 담을 수 있는 최대 무게가 가벼운 순서대로 정렬

# for i in range(n):
#     for j in bag:
#         if jewel[i][0] <= j:
#             sum += jewel[i][1]
#             bag.remove(j) # 사용된 가방 리스트에서 제거
#             break

# print(sum)
