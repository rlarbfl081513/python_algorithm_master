from collections import deque

def can_reach(limit, sy, sx, ey, ex, arr, n, m):
    q = deque()
    visited = [[False]*m for _ in range(n)]
    q.append((sy, sx))
    visited[sy][sx] = True

    while q:
        y, x = q.popleft()

        # 도착하면 True
        if (y, x) == (ey, ex):
            return True

        # 좌우로 이동 (땅에서만 1칸)
        for dx in [-1, 1]:
            ny, nx = y, x + dx
            if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] in [1,2,3] and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx))

        # 상하로 limit만큼 이동 (빈칸, 땅, 출발/도착점 포함)
        for dy in [-1, 1]:
            for l in range(1, limit+1):
                ny, nx = y + dy*l, x
                if not (0 <= ny < n and 0 <= nx < m):
                    break
                if arr[ny][nx] in [1,2,3]:
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        q.append((ny, nx))
                    # 바로 뒤가 또 빈칸일 수 있으니 for 계속
                elif arr[ny][nx] == 0:
                    continue
                else:  # 그밖의 칸 (이상값), 스킵
                    break

    return False

T = int(input())
for case in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    sy = sx = ey = ex = -1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                sy, sx = i, j
            elif arr[i][j] == 3:
                ey, ex = i, j

    limit = 1
    while True:
        if can_reach(limit, sy, sx, ey, ex, arr, n, m):
            break
        limit += 1

    print(f"#{case} {limit}")
