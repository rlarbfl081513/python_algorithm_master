
# 문제로 보는 브루트포스와 백트래킹 사용

```python
    def okay(row, visited):
    for r in range(row):
        if visited[row] == visited[r] or row - r == abs(visited[row] - visited[r]):
            return False
    return True


    def dfs(row, N, visited):
        global cnt
        if row == N:
            cnt += 1
            return

        for col in range(N):
            visited[row] = col
            if okay(row, visited):
                dfs(row + 1, N, visited)


    T = int(input())

    for t in range(1, T + 1):
        N = int(input())
        cnt = 0
        visited = [-1] * (N)

        dfs(0, N, visited)

        print(f'#{t} {cnt}')
```

좋습니다 🙂
제가 **파이썬 기초를 1달 정도 공부한 학생**이라고 생각하고, 지금 이 **N-Queen 코드**가 왜 *완전탐색(Brute Force)* & *백트래킹(Backtracking)* 단원에 있는지, 그리고 코드가 어떻게 동작하는지 아주 쉽게 설명해줄게요.

---

## 1. 문제 배경: N-Queen

* 체스의 **퀸(Queen)** 은 가로, 세로, 대각선 어디든 원하는 만큼 움직일 수 있어요.
* 그래서 체스판 위에 퀸 두 개를 놓을 때, 같은 행/열/대각선에 있으면 서로 공격할 수 있죠.
* 문제는: `N x N` 체스판에 **퀸 N개를 서로 공격하지 않게 놓는 방법이 몇 가지나 있나?**

---

## 2. 이 문제의 접근법

1. **완전탐색 (Brute Force)**
   → “모든 경우를 다 시도해본다.”
   각 행에 퀸을 하나씩 둔다고 했을 때, `row`마다 모든 `col`을 시도.

2. **백트래킹 (Backtracking)**
   → “이미 불가능한 경우는 더 보지 않고 바로 되돌아가기.”
   예를 들어 1행과 2행에 퀸을 놓았는데 서로 대각선에 있다?
   → 그럼 그 아래 행들은 더 볼 필요가 없음. 여기서 탐색을 멈추고 다른 경우를 시도.

---

## 3. 코드 이해하기

### (1) `okay(row, visited)`

```python
def okay(row, visited):
    for r in range(row):
        # 같은 열에 있으면 안 됨
        if visited[row] == visited[r]:
            return False
        # 대각선에 있으면 안 됨 (행 차이 == 열 차이)
        if row - r == abs(visited[row] - visited[r]):
            return False
    return True
```

* `visited[row]` : `row`행에 퀸을 둔 열(col)의 번호 저장
* 지금 row에 놓은 퀸이, 이전 행들(`0 ~ row-1`)의 퀸과 **충돌하지 않는지 검사**

  * 같은 열 ❌
  * 같은 대각선 ❌

---

### (2) `dfs(row, N, visited)`

```python
def dfs(row, N, visited):
    global cnt
    if row == N:         # 모든 행에 퀸을 성공적으로 놓았다면
        cnt += 1         # 해답 1개 완성
        return

    for col in range(N):         # 이번 행의 모든 열을 시도
        visited[row] = col       # row행에 col열에 퀸 놓기
        if okay(row, visited):   # 지금까지 괜찮으면
            dfs(row+1, N, visited)  # 다음 행으로 내려가기
```

* `dfs`는 한 행(row)씩 내려가며 퀸을 배치
* `okay`가 True면 다음 행으로 진행
* `okay`가 False면 더 깊이 안 내려가고, 다른 열(col)을 시도 (**백트래킹**)

---

### (3) 실행부

```python
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    cnt = 0
    visited = [-1] * N   # visited[row] = 해당 행에 퀸이 놓인 열 번호

    dfs(0, N, visited)   # 0행부터 시작

    print(f'#{t} {cnt}')
```

* 테스트 케이스 T개
* `visited` 배열 초기화 (처음엔 다 -1)
* `dfs(0, N, visited)`로 0행부터 탐색 시작
* `cnt` = 가능한 모든 해답의 개수

---

## 4. 왜 Brute Force & Backtracking 단원?

* Brute Force:
  매 행마다 모든 열(col)을 다 시도 → 경우의 수 전부 탐색.
* Backtracking:
  충돌나는 경우(`okay == False`)는 더 깊게 안 내려감 → 불필요한 탐색 줄임.

즉, **완전탐색의 뼈대 + 백트래킹의 가지치기**가 합쳐진 대표 문제라서 이 단원에 있어요.

---

## 5. 비유로 이해하기

체스판에 퀸을 한 줄씩 놓는 걸 “시험지 답안 적기”라고 해봅시다.

* Brute Force: 모든 행에 0\~N-1번 열을 다 시도 → 모든 답안 다 작성.
* Backtracking: 답안 쓰다가 규칙 위반(같은 열/대각선) 나오면 그 뒤 문제는 안 품 → 시간 절약.

---