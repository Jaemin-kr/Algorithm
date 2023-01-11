#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int board[502][502] = {
    {1,1,1,0,1,0,0,0,0,0},
    {1,0,0,0,1,0,0,0,0,0},
    {1,1,1,0,1,0,0,0,0,0},
    {1,1,0,0,1,0,0,0,0,0},
    {0,1,0,0,0,0,0,0,0,0},
    {0,0,0,0,0,0,0,0,0,0},
    {0,0,0,0,0,0,0,0,0,0}
}; //1 - blue, 0 - red

bool vis[502][502];
int n = 7, m = 10; //n은 행(가로줄, row), m은 열(세로줄, col)
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    vis[0][0] = 1; //0,0 방문
    Q.push({0,0});
    while(!Q.empty()){
        pair<int,int> cur = Q.front(); Q.pop();
        cout << '(' << cur.X << ", " << cur.Y << ") -> ";
        for(int dir = 0; dir < 4; dir++){ //상하좌우 탐색
            int nx = cur.X + dx[dir];
            int ny = cur.Y + dy[dir]; //nx, ny에 dir에서 정한 방향의 인접한 칸의 좌표가 들어감
            //dx[dir], dy[dir] = (1,0), (0,1), (-1,0), (0, -1)
            if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue; //범위 밖일 경우 넘어감
            if(vis[nx][ny] || board[nx][ny] != 1) continue; // 이미 방문한 칸이거나 파란칸이 아닌경우
            vis[nx][ny] = 1; // (nx, ny)를 방문했다고 명시
            Q.push({nx,ny}); //nx, ny를 큐에 집어넣음
        }
    }
}
