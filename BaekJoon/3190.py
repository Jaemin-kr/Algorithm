from collections import deque

def change_dir(dir, chr):
    if chr == "L":
        dir = (dir-1) % 4
    else:
        dir = (dir+1) % 4
    return dir

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def start():
    direction = 1 #초기방향
    time = 1 #시간
    y, x = 0, 0 #초기 뱀 위치
    visited = deque([[y, x]]) #뱀 방문 위치
    arr[y][x] = 2
    while True:
        y, x = y+dy[direction], x+dx[direction]
        if 0 <= y < N and 0 <= x < N and arr[y][x] != 2:
            if not arr[y][x] == 1: #사과가 없는 경우
                temp_y, temp_x = visited.popleft()
                arr[temp_y][temp_x] = 0 #꼬리 이동
            arr[y][x] = 2
            visited.append([y, x])
            if time in times.keys():
                direction = change_dir(direction, times[time])
            time += 1
        else: #몸에 부딛치거나 벽에 부딛친 경우
            return time

if __name__ == "__main__":
    N = int(input())
    K = int(input())
    arr = [[0] * N for _ in range(N)] #N x N 배열 초기화
    for _ in range(K):
        a, b = map(int, input().split()) #사과 위치
        arr[a-1][b-1] = 1 #사과 저장
    L = int(input())
    times = {}
    for i in range(L):
        X, C = input().split()
        times[int(X)] = C
    print(start())