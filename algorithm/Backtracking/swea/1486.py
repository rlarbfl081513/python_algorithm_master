## 장훈이의 높은 선반

def select_h(n, total, arr):
    global min_h
    
    # 모든 직원을 다 확인했을 시
    if n == N:
        # 토탈값이 크거나 같으면
        if total >= B:
            # 더 작은 값으로 갱신
            min_h = min(min_h, total)
        return
    # 토탈값이 아직 작으면
    if total < min_h:
        # n번째 직원을 선택하지 '않고' 넘어감
        select_h(n + 1, total, arr)
        # n번째 직원을 선택하고  '  ' 넘어감
        select_h(n + 1, total+arr[n], arr)
 
 
T = int(input())
 
for t in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
 
    min_h = sum(arr)
 
    select_h(0, 0, arr)
 
    print(f'#{t} {min_h - B}')