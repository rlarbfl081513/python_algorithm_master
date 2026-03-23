
from collections import deque

def find_fr(k):
    # 방문 여부와 거리를 동시에 저장할 배열 (-1은 아직 방문 안 함을 의미)
    distances = [-1] * (n + 1)
    distances[k] = 0  # 자기 자신(시작점)과의 거리는 0
    
    q = deque([k]) # 큐에 시작점만 넣고 출발!
    
    while q:
        current = q.popleft()
        
        # 현재 사람과 연결된 모든 친구를 확인
        for friend in fr[current]:
            # 아직 방문하지 않은 친구라면 (최단 거리 발견!)
            if distances[friend] == -1:
                # 나까지 오는 데 걸린 거리 + 1을 기록
                distances[friend] = distances[current] + 1
                q.append(friend)
                
    # BFS가 끝나면 distances 배열에는 k에서 모든 사람까지의 최단 거리가 들어있습니다.
    # 0번 인덱스는 안 쓰니까 [1:]로 슬라이싱해서 1~N번까지의 합을 구합니다.
    return sum(distances[1:])

n, m = map(int, input().split(" "))
fr = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split(" "))
    fr[a].append(b) # 리스트 덧셈(+) 대신 append()를 쓰면 속도가 더 빠릅니다!
    fr[b].append(a)

bacon = [0] # 0번 인덱스 채우기용

# 1번 사람부터 n번 사람까지 케빈 베이컨의 수를 구함
for j in range(1, n + 1):
    bacon.append(find_fr(j))

# 작성하셨던 최솟값 및 인덱스 찾기 로직 (아주 좋습니다!)
minnum = bacon[1]
index = 1

for a in range(2, n + 1):
    if minnum > bacon[a]:
        minnum = bacon[a]
        index = a

print(index)