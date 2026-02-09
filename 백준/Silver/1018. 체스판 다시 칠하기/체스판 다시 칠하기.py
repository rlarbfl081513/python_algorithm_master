
def check_min(a,b,new):

    cnt = 0
    start = new[a][b]

    for x in range(a, a + 8):
        for y in range(b,b+8):
            # 짝수인데 시작이랑 같은 거면 안바꿔도됨
            if (x+y)%2 == 0 and new[x][y] != start:
                cnt += 1
            elif (x+y)%2 != 0 and new[x][y] == start:
                cnt += 1

    minmin = min(cnt, 64-cnt)


    return minmin


n,m = map(int,input().split())
board = [list(input()) for _ in range(n)]
min_num = float('inf')

for i in range(n-8+1):
    for j in range(m-8+1):
        new_min = check_min(i,j,board)
        min_num = min(min_num, new_min)

print(min_num)