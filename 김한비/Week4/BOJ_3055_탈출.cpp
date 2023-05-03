#include <iostream>
#include <queue>

using namespace std;

int R, C;
int map[50][50];
bool visited[50][50];
int cnt[50][50];
int water_map[50][50];
bool water_visited[50][50];

int dx[4] = { 1, -1, 0, 0 };
int dy[4] = { 0, 0, 1, -1 };

pair<int, int> s;
pair<int, int> d;
queue<pair<int, int>> water;


void water_bfs() {

	while (!water.empty()) {
		int xx = water.front().first;
		int yy = water.front().second;

		water.pop();
		for (int i = 0; i < 4; i++) {
			int nx = xx + dx[i];
			int ny = yy + dy[i];

			if (nx >= 0 && nx < R && ny >= 0 && ny < C && map[nx][ny] == 0 && !water_visited[nx][ny]) {
				water.push({ nx, ny });
				water_visited[nx][ny] = true;
				water_map[nx][ny] = water_map[xx][yy] + 1;
			}
		}
	}
}


void bfs(int x, int y) {
	visited[x][y] = true;
	cnt[x][y]++;

	queue<pair<int, int>> q;
	q.push({ x, y });

	while (!q.empty()) {
		int xx = q.front().first;
		int yy = q.front().second;

		q.pop();
		for (int i = 0; i < 4; i++) {
			int nx = xx + dx[i];
			int ny = yy + dy[i];

			if (nx >= 0 && nx < R && ny >= 0 && ny < C && map[nx][ny] == 0 && !visited[nx][ny]) {
				q.push({ nx, ny });
				visited[nx][ny] = true;
				cnt[nx][ny] = cnt[xx][yy] + 1;
			}
		}
	}

}


int main() {

	cin >> R >> C;
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			char tmp;
			cin >> tmp;
			if (tmp == 'X')	map[i][j] = 1; //돌
			else if (tmp == '*') { //물
				water_map[i][j] = 1;
				water.push({ i, j });
				water_visited[i][j] = true;
			}
			else if (tmp == 'S')	s = { i, j }; //시작점
			else if (tmp == 'D') { //도착점
				map[i][j] = 1;
				d = { i, j };
			}

		}
	}

	water_bfs();
	bfs(s.first, s.second);

	int ans = 100001;
	for (int i = 0; i < 4; i++) {
		int nx = d.first + dx[i];
		int ny = d.second + dy[i];
		if (nx < 0 || nx >= R || ny < 0 || ny >= C) continue; //범위 벗어난 경우
		if (water_map[nx][ny] > 0 && cnt[nx][ny] >= water_map[nx][ny]) continue; //물로 채워진 경우
		if (cnt[nx][ny] == 0) continue; //도달할 수 없는 경우
		ans = min(ans, cnt[nx][ny]);
	}
	if (ans == 100001)
		cout << "KAKTUS";
	else
		cout << ans;

	return 0;
}
