import sys
input = sys.stdin.readline

n = int(input())
arr = []

# 리스트 컴프리헨션보다 append가 가독성이 좋고, 
# 데이터가 많을 땐 sys.stdin.read().split() 등을 활용하기도 합니다.
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort()

# 출력 최적화: 리스트의 각 원소를 문자열로 바꿔 한 번에 출력
for i in arr:
    sys.stdout.write(f"{i[0]} {i[1]}\n")