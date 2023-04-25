import sys

input = sys.stdin.readline

n = int(input())
cnt = 0

incar = [input().strip() for _ in range(n)]
outcar = [input().strip() for _ in range(n)]

for car in outcar:
  if car != incar[0]:
    cnt += 1
    incar.remove(car)
  else:
    incar.remove(car)

print(cnt)
