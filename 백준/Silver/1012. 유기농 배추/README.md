# [Silver II] 유기농 배추 - 1012 

[문제 링크](https://www.acmicpc.net/problem/1012) 

### 성능 요약

메모리: 32412 KB, 시간: 192 ms

### 분류

그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색, 격자 그래프, 플러드 필

### 제출 일자

2026년 2월 24일 10:31:11

### 문제 설명

<p>차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다. 농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에, 한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다. 이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다. 특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다. 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.</p>

<p>한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다. 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다. 예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다. 0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.</p>

<table class="table table-bordered" style="width:40%">
	<tbody>
		<tr>
			<td style="text-align:center; width:4%"><strong>1</strong></td>
			<td style="text-align:center; width:4%"><strong>1</strong></td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
		</tr>
		<tr>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%"><strong>1</strong></td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
		</tr>
		<tr>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%"><strong>1</strong></td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
		</tr>
		<tr>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%"><strong>1</strong></td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
		</tr>
		<tr>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%"><strong>1</strong></td>
			<td style="text-align:center; width:4%"><strong>1</strong></td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%"><strong>1</strong></td>
			<td style="text-align:center; width:4%"><strong>1</strong></td>
			<td style="text-align:center; width:4%"><strong>1</strong></td>
		</tr>
		<tr>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%"><strong>1</strong></td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%">0</td>
			<td style="text-align:center; width:4%"><strong>1</strong></td>
			<td style="text-align:center; width:4%"><strong>1</strong></td>
			<td style="text-align:center; width:4%"><strong>1</strong></td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.</p>

### 출력 

 <p>각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.</p>


---
```
## BFS(너비 우선 탐색) vs DFS(깊이 우선 탐색) 정리

### 1. 알고리즘 비교 요약

| 구분 | BFS (Breadth-First Search) | DFS (Depth-First Search) |
| --- | --- | --- |
| **데이터 구조** | **큐 (Queue)** | **스택 (Stack)** 또는 재귀 함수 |
| **처리 원칙** | **FIFO (First-In, First-Out)** | **LIFO (Last-In, First-Out)** |
| **탐색 방식** | 현재 노드에서 **인접한 노드**를 먼저 방문 | 한 방향으로 **갈 수 있는 끝까지** 탐색 |
| **주요 용도** | 최단 경로 탐색, 레벨 순회 | 경로 존재 여부 확인, 모든 경우 탐색 |

---

### 2. Queue를 이용한 BFS (너비 우선 탐색)

가장 가까운 노드부터 넓게 퍼져나가며 탐색하는 방식입니다.

* **동작 원리**:
1. 탐색 시작점을 큐에 삽입하고 방문 처리한다.
2. 큐에서 노드를 꺼내 인접한 노드 중 방문하지 않은 노드를 **큐의 뒤(append)에 모두 넣고** 방문 처리한다.
3. 큐가 빌 때까지 반복한다.


* **코드 특징**:
* `collections.deque` 객체를 사용하여 `popleft()`로 선입선출을 구현한다.
* 인접한 칸들을 먼저 다 넣기 때문에 "물결이 퍼져나가는 듯한" 탐색을 수행한다.



```python
# BFS 예시 (Queue 사용)
qu = deque([[i, j]])
field[i][j] = 2 # 시작점 방문 처리

while qu:
    a, b = qu.popleft() # 가장 먼저 들어온 것부터 추출
    for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ny, nx = a + dy, b + dx
        if 0 <= ny < n and 0 <= nx < m and field[ny][nx] == 1:
            qu.append([ny, nx]) # 뒤로 삽입
            field[ny][nx] = 2

```

---

### 3. Stack을 이용한 DFS (깊이 우선 탐색)

한 경로를 끝까지 파고든 후, 더 이상 갈 곳이 없으면 되돌아와서 다른 경로를 찾는 방식입니다.

* **동작 원리**:
1. 탐색 시작점을 스택에 삽입하고 방문 처리한다.
2. 스택에서 노드를 꺼내 인접한 노드 중 방문하지 않은 노드를 **스택의 끝(append)에 넣고** 방문 처리한다.
3. 스택이 빌 때까지 반복한다. (가장 마지막에 넣은 노드가 다음 루프에서 바로 추출됨)


* **코드 특징**:
* 일반 List의 `append()`와 `pop()`을 사용하여 후입선출을 구현한다.
* 가장 최근에 발견한 경로를 우선적으로 파고든다.



```python
# DFS 예시 (Stack 사용)
stack = [[i, j]]
field[i][j] = 2 # 시작점 방문 처리

while stack:
    a, b = stack.pop() # 가장 마지막에 들어온 것부터 추출
    for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ny, nx = a + dy, b + dx
        if 0 <= ny < n and 0 <= nx < m and field[ny][nx] == 1:
            stack.append([ny, nx]) # 뒤로 삽입
            field[ny][nx] = 2

```

---

### 4. 주의사항 (Common Pitfalls)

1. **시작점 방문 처리**: 큐나 스택에 넣기 전에(또는 넣은 직후에) 반드시 시작 좌표를 방문 처리(`field[i][j] = 2`)해야 중복 탐색 및 무한 루프를 방지할 수 있습니다.
2. **데이터 구조의 선택**:
* 유기농 배추 문제처럼 단순히 연결된 뭉텅이(Island)의 개수를 세는 문제에서는 BFS와 DFS 중 어느 것을 사용해도 결과는 같습니다.
* 단, 미로 찾기 등에서 **최단 거리**를 구해야 할 때는 반드시 **BFS**를 사용해야 합니다.
```

