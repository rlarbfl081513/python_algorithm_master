
# 며칠이 지나면 토마토들이 모두 익는지 최소 일수 구하기
# 어떤 칸에는 토마토가 없을수도
from collections import deque

def burn():
    total = 0
    q = deque(good)

    while q:
        kk,yy,xx= q.popleft()

        total = max(total,tomato_box[kk][yy][xx])
        # 익은 토마토를 찾으면 익혀야하는데. 그럼 일수는?
        for a,b,c in [[0,-1,0],[0,1,0],[1,0,0],[-1,0,0],[0,0,1],[0,0,-1]]:
            ny,nx,nk = a+yy,b+xx,c+kk
            if 0 > ny or n <= ny or 0 > nx or m <= nx or 0 > nk or h <= nk:
                continue
            if tomato_box[nk][ny][nx] == 0:
                tomato_box[nk][ny][nx] = tomato_box[kk][yy][xx] + 1 # 익히기
                q.append([nk,ny,nx])

    return total


m,n,h = map(int,input().split(" "))
tomato_box = []
for _ in range(h):
    tomato_box.append([list(map(int,input().split(" "))) for _ in range(n)])

good = []
cnt_t = 0
for q in range(h):
    for w in range(n):
        for e in range(m):
                if tomato_box[q][w][e] == 1:
                    cnt_t += 1
                    good.append([q,w,e])

if cnt_t == m*n*h:
    print(0)
else:
    result = burn()

    cnt_z = 0
    cnt_t = 0

    for q in range(h):
        for w in range(n):
            for e in range(m):
                if tomato_box[q][w][e] == 0:
                    cnt_z += 1
                else:
                    cnt_t += 1

    # 이미 다 익어있으면 : 모두 1
    # 모두 익지 못하면 : 모두 0

    if cnt_z == m*n*h or cnt_t < m*n*h:
        print(-1)
    else:
        print(result-1)

