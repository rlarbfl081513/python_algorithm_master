# 첫번쨰 방법

# n = int(input())
# val = 0
#
# # 1부터 주어진 n이 될때까지 1씩더하면서 연속된 6이 들어있는지 확인하기
# for i in range(1,n+1):
#     while True:
#         val += 1
#         # 문자열로 변환하여 연속된 6덩어리가 있는지 확인
#         if "666" in str(val) or "6666" in str(val) or "66666" in str(val):
#             break
#
# print(val)


# 두번째 방식

n = int(input())
val = 0
cnt = 0

while True:
    val += 1
    if "666" in str(val):
        cnt += 1

    if cnt == n:
        print(val)
        break