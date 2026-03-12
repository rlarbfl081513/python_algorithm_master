def home(x,y):
    global li,total,box

    go = [[i,j]]
    cnt = 0

    while go:
        xx,yy = go.pop()
        li[xx][yy] = 'a'
        if box[xx][yy] == 1:
            continue

        box[xx][yy] = 1
        cnt += 1

        for a in [[0,1],[0,-1],[1,0],[-1,0]]:
            nx,ny = xx+a[0], yy+a[1]

            if 0 > nx or n <= nx or 0 > ny or n <= ny:
                continue

            if li[nx][ny] == '1' and box[nx][ny] == 0:
                go.append([nx,ny])
    return cnt



n = int(input())
li = [list(map(str, input())) for _ in range(n)]
box = [[0]*n for _ in range(n)]
total = 0
to_li =[]


for i in range(n):
    for j in range(n):
        if li[i][j] == '1':
            to_li.append(home(i,j))
            total += 1

to_li.sort()
print(total)

for k in to_li:
    print(k)
