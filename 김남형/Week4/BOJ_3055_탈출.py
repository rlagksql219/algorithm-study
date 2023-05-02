from collections import deque

r, c = map(int, input().split())

graph = [list(input()) for _ in range(r)] # 그래프 생성
distance = [[0] * c for _ in range(r)] # 거리 값 리스트 생성

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

def bfs(Gx, Gy):
    while q:
        x, y = q.popleft() # queue에서 값 꺼내기
        
        if graph[Gx][Gy] == 'S': # 목적지에 'S'가 도착하면 시작점으로부터 거리 값 출력
            return distance[Gx][Gy]
    
        for i in range(4): # 상하좌우 이동
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c: # 이동한 위치가 그래프를 벗어나지 않으면
                if (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and graph[x][y] == 'S': # 현재 위치가 'S'이고 이동한 위치에 물과 돌이 없으면
                    graph[nx][ny] = 'S' # 'S'를 이동한 위치에 이동
                    distance[nx][ny] = distance[x][y] + 1 # 이동한 거리 증가
                    q.append((nx, ny)) # 이동한 위치 queue에 삽입
                
                elif (graph[nx][ny] == '.' or graph[nx][ny] == 'S') and graph[x][y] == '*': # 현재 위치가 '*'이고 이동한 위치에 목적지와 돌이 없으면
                    graph[nx][ny] = '*' # '*'을 이동한 위치에 이동
                    q.append((nx, ny)) # 이동한 위치 queue에 삽입
    
    return 'KAKTUS' # 'S'가 목적지에 도착하지 못하면 'KAKTUS' 반환

# 시작점 queue에 넣고, 목적지 값 대입
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            q.append((i, j))
        elif graph[i][j] == 'D':
            Gx, Gy = i, j   # 목적지 Goal_x, Goal_y

# 물이 있는 곳 queue에 넣기 (시작점을 먼저 queue에 넣어야 하기 때문에 반복문 따로 작성)
for i in range(r):
    for j in range(c):
        if graph[i][j] == '*':
            q.append((i, j))

print(bfs(Gx, Gy))
