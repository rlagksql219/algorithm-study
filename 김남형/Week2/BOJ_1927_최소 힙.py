import sys
import heapq

n = int(sys.stdin.readline())
heap = []
data = 0

for _ in range(n):
  data = int(sys.stdin.readline().rstrip())
  if data != 0:
    heapq.heappush(heap, data)
  else:
    try:
      print(heapq.heappop(heap))
    except:
      print(0)
