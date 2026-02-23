def fibonacci(m):
    if m == 0 or m == 1:
        return 1

    if memo[m]:
        return  memo[m]

    memo[m] = fibonacci(m-1) + fibonacci(m-2)
    return memo[m]


n = int(input())
memo = [0]*n


if n == 1:
    print(fibonacci(1) % 10007)
else:
    memo[0], memo[1] = 1, 1
    # 맨 오른쪽에 가로의 길이가 각각 2,1인 사각형으로 끝날때
    sero = fibonacci(n-1)
    garo = fibonacci(n-2)
    all_result = garo + sero

    print(all_result % 10007)