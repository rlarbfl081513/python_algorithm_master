n = int(input())
arr = list(list(map(int,input().split(" "))) for _ in range(n))
arr.sort()

for i in arr:
    print(i[0],i[1])