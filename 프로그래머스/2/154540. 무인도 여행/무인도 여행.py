def solution(maps):
    total = []
    a = len(maps)
    bb = len(maps[0])
    visit = list([0]*bb for _ in range(a))
    maps = list( list(k) for k in maps)
    # 지도를 돌면서 땅이면 0으로 바꾸면서 일수 세기
    for i in range(a):
        for j in range(bb):
             if maps[i][j] != 'X' and visit[i][j] == 0:
                       visit[i][j] = 1
                       smu = int(maps[i][j])
                       
                       go = [[i,j]]
                       while len(go) > 0:
                            x,y = go.pop()
                            for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                                nx,ny = x+dx,y+dy
                                if nx < 0 or nx >= a or ny < 0 or ny >= bb :
                                    continue
                                    
                                if maps[nx][ny] != 'X' and visit[nx][ny] == 0:
                                    visit[nx][ny] = 1
                                    smu += int(maps[nx][ny])
                                    go.append([nx,ny])
                       total.append(smu)
    total.sort()   
    if len(total) == 0:
        return [-1]
    else:
        return total
                       