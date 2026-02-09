def math_class():
    a, b, c, d, e, f = map(int, input().split())

    for i in range(-999,1000):
        for j in range(-999,1000):
            if a*i + b*j == c and d*i + e*j == f:
                return i, j





x,y = math_class()
print(x, y)