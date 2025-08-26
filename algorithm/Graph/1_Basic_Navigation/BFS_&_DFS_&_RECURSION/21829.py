## 큐덱 사용
from collections import deque

for tc in range(1,int(input())+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    queue = deque()
    visit = [0]*n

    queue.append(0)
    visit[0] = 1
    print(0, end=" ")

    while queue:
        a = queue.popleft()

        for i in range(n):
            if visit[i] == 0 and arr[a][i] == 1:
                visit[i] = 1
                queue.append(i)
                print(i, end=" ")

    print()
    


## 딕셔너리를 사용
from collections import  deque

def dfsDict(key):
    global dict, n, visit, num


    for i in dict.get(key,[]):
        if num[i] == 0:
            visit.append(i)
            num[i] = 1
            print(i, end=" ")

    if visit :
        start = visit.popleft()
        dfsDict(start)

for tc in range(1,int(input())+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    dict = {}

    # 딕셔너리 형태로 바꾸기
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                # 해당 키가 없으면 키와 값을 넣기, 이미 있었다면 해당 리스트에 추가하기
                dict[i] = dict.get(i,[]) + [j]
    print(dict)
    # 방문 리스트
    visit = deque()
    num = [0]*n
    num[0] = 1

    ## 아래 두가지는 딕셔너리의 첫 키를 가져오는 방식
    start = next(iter(dict))
    # first_key = list(dict.keys())[0]

    print(f'#{tc}',end=" ")
    print(start, end=" ")
    dfsDict(start)
    print()