import sys
input = sys.stdin.readline
from collections import deque


n,m = map(int,input().split())
arr = [list(map(int,input().split(" "))) for _ in range(n)]
visit = [[-1]*m for _ in range(n)]
q = deque([])

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            q.append([i,j])
            visit[i][j] = 0
        elif arr[i][j] == 0:
            visit[i][j] = 0

while q:
    ny,nx = q.popleft()

    for i in [[0,1],[0,-1],[1,0],[-1,0]]:
        nny,nnx = ny+i[0],nx+i[1]

        # 범위 넘어가면 아웃
        if 0 > nny or n <= nny or 0 > nnx or m <= nnx:
            continue

        if visit[nny][nnx] == -1 and arr[nny][nnx] == 1:
            visit[nny][nnx] = visit[ny][nx] + 1
            q.append([nny,nnx])


for i in visit:
    print(" ".join(map(str,i)))
