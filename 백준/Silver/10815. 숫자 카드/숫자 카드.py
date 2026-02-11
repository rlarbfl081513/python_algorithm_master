import sys

# 입력 속도 가속
input = sys.stdin.readline

# 방법 1 : 시간초과
# n = int(input())
# n_arr = list(map(int, input().split(" ")))
#
# m = int(input())
# m_arr = list(map(int, input().split(" ")))
#
# new = n_arr+m_arr
#
# # 중복된 값은 다 지워버리기
# result = set(i for i in new if new.count(i) == 1)
#
# for j in m_arr:
#     if j in result:
#         print(0, end=" ")
#     else:
#         print(1, end=" ")


## 방법 2
# 시간 복잡도: O(N + M)
# set 생성: O(N) 
# m_arr 순회 및 탐색: M * O(1) = O(M)
# 특징: 파이썬에서 가장 빠르고 직관적인 방법임.

n = int(input())
n_arr = set(list(map(int, input().split(" "))))

m = int(input())
m_arr = list(map(int, input().split(" ")))

for i in m_arr:
    if i in n_arr:
        print(1, end=" ")
    else:
         print(0, end=" ")
         
