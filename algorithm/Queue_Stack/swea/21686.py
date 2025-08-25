def word(n):
    count = 0

    while n != 1:
        if n % 2 != 0: # 홀수
            n = n * 3 + 1
        else: # 짝수
            n = n // 2

        count += 1

    return count

for tc in range(1,int(input())+1):
    num = int(input())
    print(f'#{tc}',word(num))