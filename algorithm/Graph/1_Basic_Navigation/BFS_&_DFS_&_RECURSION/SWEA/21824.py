## 재귀함수를 이용한 dfs
def dfs(start,lv):
    if lv == 2:
        print(*stack)
        return

    for i in range(n):
        if arr[start][i] == 1:
            stack.append(i)
            dfs(i,lv+1)
            stack.pop()


for tc in range(1,int(input())+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    stack = [0]
    print(f'#{tc}')

    # node, lv
    dfs(0,0)



##  딕셔너리를 이용해서 dfs 활용
def box(start,lv,par):
    global dict

    if lv == 2:
        print(" ".join(map(str,par)),end=" ")
        print(start, end=" ")
        print()
        return
    else:
        par.append(start)

    for new in dict.get(start,[]):
        box(new,lv+1,par)

    par.clear()
    # par = []


for tc in range(1,int(input())+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    dict = {}

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                dict[i] = dict.get(i,[]) + [j]

    parent = []

    print(f'#{tc}')
    for i in dict.get(0,[]):
        box(i,1,[0])