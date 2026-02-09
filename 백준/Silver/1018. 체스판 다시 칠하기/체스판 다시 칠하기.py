def check_min(a,b,new):

    minmin = float('inf')

    for two in ['W','B']:
        check = [row[:] for row in new]
        cnt = 0
        if check[a][b] != two:
            if check[a][b] == 'W':
                check[a][b] = 'B'
                cnt += 1
            else:
                check[a][b] = 'W'
                cnt += 1

        for x in range(a,a+8):
            for y in range(b,b+8):
                #델타를 통해 오른쪽과 아랫칸 하나씩 확인
                for q,w in [(0,1),(1,0)]:
                    nx,ny = x + q, y + w

                    # 범위를 넘으면 건너뛰기
                    if nx < 0 or ny < 0 or nx >= a+8 or ny >= b+8:
                        continue

                    if check[x][y] == 'W'and check[nx][ny] == 'W':
                            check[nx][ny] = 'B'
                            cnt += 1
                    elif check[x][y] == 'B'and check[nx][ny] == 'B':
                            check[nx][ny] = 'W'
                            cnt += 1

        minmin = min(minmin, cnt)

    return minmin




n,m = map(int,input().split())
board = [list(input()) for _ in range(n)]
min_num = float('inf')

# 8*8의 크기로 볼 시작점 정하기
for i in range(n-8+1):
    for j in range(m-8+1):
        new_board = [row[:] for row in board]
        new_min = check_min(i,j,new_board)
        min_num = min(min_num, new_min)

print(min_num)