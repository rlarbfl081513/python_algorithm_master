
# 방법 2.
import bisect
# bisect_left는 "이미 정렬된 리스트에서 특정 숫자가 들어갈 수 있는 가장 왼쪽 인덱스"를 광속으로 찾아주는 도구
# 리스트가 [10, 15, 17, 20]이고 내가 16으로 자르기로 했다면, 16보다 큰 나무는 17부터임. 
# bisect_left를 쓰면 이 위치(인덱스 2)를 O(\log N)만에 바로 알려wna

def cut():
    start = 0
    end=  max(trees)
    result = 0

    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + trees[i]

    # 2. 이진 탐색 while문 내부
    while start <= end:
        mid = (start + end) // 2

        # [수정된 부분] mid보다 큰 나무가 시작되는 위치를 찾음
        idx = bisect.bisect_left(trees, mid)

        # [수학적 계산] 루프 없이 한 번에 합 구하기
        # (전체 합 - idx까지의 합) - (남은 나무 개수 * mid)
        cnt = (prefix_sum[n] - prefix_sum[idx]) - (n - idx) * mid
        # 총합이 클 때 -> 너 높이 잘라보자
        if cnt >= m:
            # 일단 현재 칼 높이 저장
            result = mid
            start = mid+1 # 오른쪽 절반으로 점프
        else:
            # 나무가 부족
            end = mid - 1 # 왼쪽 절반으로 점프

    return result

n,m = map(int,input().split(" "))
trees = list(map(int,input().split(" ")))
total_tree = sum(trees)
trees.sort()

print(cut())
# print('result: ',cut())
# print('tree: ', trees)

