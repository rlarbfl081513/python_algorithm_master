
import sys
from collections import deque

# 입력을 빠르게 받기 위해 sys.stdin.readline 사용
input = sys.stdin.readline


def solve():
    m, n, h = map(int, input().split())
    arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

    queue = deque()

    # 1. 동시에 시작할 모든 익은 토마토를 큐에 삽입
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == 1:
                    queue.append((i, j, k))

    # 6방향 탐색을 위한 이동 설정 (위, 아래, 상, 하, 좌, 우)
    dz = [1, -1, 0, 0, 0, 0]
    dx = [0, 0, 1, -1, 0, 0]
    dy = [0, 0, 0, 0, 1, -1]

    # BFS 시작
    while queue:
        zz, xx, yy = queue.popleft()

        for i in range(6):
            nz = zz + dz[i]
            nx = xx + dx[i]
            ny = yy + dy[i]

            # 범위 내에 있고, 익지 않은 토마토(0)인 경우
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                if arr[nz][nx][ny] == 0:
                    # 익음 처리하고 날짜를 (이전 값 + 1)로 기록
                    arr[nz][nx][ny] = arr[zz][xx][yy] + 1
                    queue.append((nz, nx, ny))

    # 결과 계산
    max_day = 0
    for layer in arr:
        for row in layer:
            for cell in row:
                # 하나라도 익지 않은 토마토가 남아있다면 -1 출력 후 종료
                if cell == 0:
                    print(-1)
                    return
                max_day = max(max_day, cell)

    # 처음 시작 값이 1이었으므로 1을 빼줘야 실제 경과 일수가 됨
    # 만약 모든 토마토가 처음부터 익어있었다면 max_day는 1이므로 결과는 0
    print(max_day - 1)


solve()