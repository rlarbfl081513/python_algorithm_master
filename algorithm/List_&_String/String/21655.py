
# 1. 받은 2차배열을 딕셔너리 형태로 바꾸는 것
def word(n,arr):
    global dict

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                dict[i] = dict.get(i,[]) + [j]

    first_key = next(iter(dict))

    return dfs(first_key)

# 2. DFS로 딕셔너리 돌기
def dfs(num):
    global dict

    visit[num] = 1
    print(num,end=" ")
    li = dict.get(num,[])
    li.sort()
    for i in li:
        if visit[i]:
            continue
        dfs(i)


for tc in range(1,int(input())+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    visit = [0]*n
    dict = {}
    print(f'#{tc}',end=" ")
    word(n,arr)
    print()