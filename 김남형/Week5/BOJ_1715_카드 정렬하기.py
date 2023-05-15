import heapq
import sys

input = sys.stdin.readline

cards = []
card = 0
ans = 0

n = int(input())

for _ in range(n):
    heapq.heappush(cards, int(input()))

while cards:
    card = 0
    try:       
        for _ in range(2):
            card += heapq.heappop(cards)
    except:
        print(ans)
        break
    
    heapq.heappush(cards, card)
    ans += card
