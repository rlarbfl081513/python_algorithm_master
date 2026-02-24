
def bachu():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 0 or field[i][j] == 2:
                continue

            cnt += 1
            stack = [[i,j]]
            while stack:
                a,b = stack.pop()
                for w,e in [[0,1],[0,-1],[1,0],[-1,0]]:
                    ny,nx = a+w,b+e
                    if ny < 0 or ny >=n or nx < 0 or nx >= m:
                        continue
                    if field[ny][nx] == 0 or field[ny][nx] == 2:
                        continue
                    stack.append([ny,nx])
                    field[ny][nx] = 2

    return cnt

for tc in range(int(input())):
    m,n,k = map(int, input().split(" "))
    field = [[0]*m for _ in range(n)]
    for i in range(k):
        x,y = map(int,input().split(" "))
        field[y][x] = 1

    print(bachu())