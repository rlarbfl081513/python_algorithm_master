import sys
sys.stdin = open("input.txt")

# 2382

def flip_dir(d: int) -> int:
    # 1<->2, 3<->4
    return d + 1 if d % 2 else d - 1

# 같은 위치에 있는 것들은 합치고(수 합), 방향은 최대 군집의 방향
def merge(cells):
    N = len(cells)
    for a in range(N):
        for b in range(N):
            if len(cells[a][b]) >= 2:
                groups = cells[a][b]
                total = 0
                max_cnt, way = -1, 0
                for y, x, cnt, d in groups:
                    total += cnt
                    if cnt > max_cnt:
                        max_cnt = cnt
                        way = d
                # 해당 좌표에 하나의 리스트만 들어가게 교체
                cells[a][b] = [[a, b, total, way]]
    return cells

# 약(가장자리)에 있으면 반감 + 방향 반전, 0이면 제거
def pill(cells):
    N = len(cells)
    for a in range(N):
        for b in range(N):
            if not cells[a][b]:
                continue
            new_groups = []
            for y, x, cnt, d in cells[a][b]:
                if (y, x) in killzone:
                    cnt //= 2
                    d = flip_dir(d)
                if cnt > 0:
                    new_groups.append([y, x, cnt, d])
            cells[a][b] = new_groups
    return cells

# 이동: 좌표만 바꾸는 게 아니라, 실제 버킷을 새 위치로 옮겨야 함
# (기존 구조 유지: move -> pill -> merge 순으로 동작, 최종 cells 반환)
def move(cells):
    N = len(cells)
    next_cells = [[[] for _ in range(N)] for _ in range(N)]
    for j in range(N):
        for i in range(N):
            for y, x, cnt, d in cells[j][i]:
                ny, nx = y, x
                if d == 1:   ny -= 1  # 상
                elif d == 2: ny += 1  # 하
                elif d == 3: nx -= 1  # 좌
                elif d == 4: nx += 1  # 우
                next_cells[ny][nx].append([ny, nx, cnt, d])

    # 기존 흐름 살리기: 이동 후 약 처리 -> 병합
    pill(next_cells)
    merge(next_cells)
    return next_cells

for tc in range(1, int(input()) + 1):
    n, m, k = map(int, input().split())          # n: 격자, m: 시간, k: 군집 수
    cells = [[[] for _ in range(n)] for _ in range(n)]
    for _ in range(k):
        y, x, c, d = map(int, input().split())   # 방향 변수 이름을 d로 (기존 k와 충돌 방지)
        cells[y][x].append([y, x, c, d])

    # 가장자리(약) 좌표 집합
    killzone = set()
    for a in range(n):
        killzone.add((0, a))
        killzone.add((n - 1, a))
        killzone.add((a, 0))
        killzone.add((a, n - 1))

    # 주어진 횟수만큼 순환 (move -> pill -> merge가 move 내부에서 수행됨)
    for _ in range(m):
        cells = move(cells)

    # 총합
    total = 0
    for a in range(n):
        for b in range(n):
            for _, _, cnt, _ in cells[a][b]:
                total += cnt

    print(f'#{tc} {total}')
