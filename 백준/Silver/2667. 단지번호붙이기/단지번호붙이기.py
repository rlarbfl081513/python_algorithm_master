

def home(x,y):

    go = [[x,y]]
    cnt = 0

    while go:
        xx,yy = go.pop()
        li[xx][yy] = 0
        cnt += 1

        for a in [[0,1],[0,-1],[1,0],[-1,0]]:
            nx,ny = xx+a[0], yy+a[1]

            if 0 > nx or n <= nx or 0 > ny or n <= ny:
                continue

            if li[nx][ny] == '1':
                li[nx][ny] = 0
                go.append([nx,ny])
    return cnt



n = int(input())
li = [list(input()) for _ in range(n)]
to_li =[]


for i in range(n):
    for j in range(n):
        if li[i][j] == '1':
            to_li.append(home(i,j))

to_li.sort()
print(len(to_li))

for k in to_li:
    print(k)

