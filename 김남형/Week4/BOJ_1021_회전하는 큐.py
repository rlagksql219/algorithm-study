from collections import deque

n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

q = deque()
for i in range(1, n+1):
    q.append(i)

for i in arr:
    while True:
        if i == q[0]:
            q.popleft()
            break
        elif q.index(i) <= len(q) // 2:
            q.rotate(-1)
            cnt += 1
        else : # elif q.index(i) > len(q) // 2:
            q.rotate(1)
            cnt += 1
            
print(cnt)

# pop 해야 할 값이 가운데보다 왼쪽에 있으면 오른쪽으로 rotate 해주고 오른쪽에 있으면 왼쪽으로 rotate 해준다.
# rotate 할 때마다 cnt 증가
