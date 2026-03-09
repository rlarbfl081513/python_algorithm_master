

# 재귀함수로 해서 계속해서 나누고나누게 하면 되지 않을까'?

def cut(x1,x2,y1,y2):
    global w_p,b_p
    # print('시작 x',x1 ,'~',x2,'시작 y', y1, '~', y2)
    # print()

    # 종료조건
    if x2 - x1 == 1:
        if arr[x1][y1] == 0:
            w_p += 1
            return
        else:
            b_p += 1
            return

    ww,bb = 0,0
    for i in range(x1,x2):
        for j in range(y1,y2):
            if arr[i][j] == 0:
                ww += 1
            else:
                bb += 1

    # 하나의 색만 존재한다면 - 패스
    if 0 in [ww,bb]:
        if ww != 0:
            w_p += 1
        elif bb != 0:
            b_p += 1
        return
    # 만약 해당 면적에 두개의 색이 존재한다면 - 자르기 진행
    else:
        xx,yy = (x2-x1)//2, (y2-y1)//2
        return cut(x1,x1+xx,y1,y1+yy),cut(x1,x1+xx,y1+yy,y2),cut(x1+xx,x2,y1,y1+yy),cut(x1+xx,x2,y1+yy,y2)


n = int(input())
arr = [list(map(int,input().split(" "))) for _ in range(n)]
w_p,b_p = 0,0 # 흰종이, 파란종이

cut(0,n,0,n)

print(w_p)
print(b_p)