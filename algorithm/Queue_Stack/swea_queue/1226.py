from collections import deque

def miro(ni):
    queue = deque()
    queue.append((1,1))

    while queue:
        a,b = queue.popleft()

        for y,x in [[0,1],[0,-1],[1,0],[-1,0]]:
            ny, nx = a + y, b + x
            ii = ni[ny][nx]
            if 0 <= ny < 16 and 0 <= nx < 16 and ni[ny][nx] != 1:
                if ni[ny][nx] == 3:
                    return 1
                queue.append((ny,nx))
                ni[ny][nx] = 1

    return 0

for tc in range(1,11):
    n = int(input())
    arr = [list(map(int,input())) for _ in range(16)]

    print(f'#{tc}', miro(arr))