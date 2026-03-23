

from collections import deque

def find_fr(k):
    total = 0
    start = []

    for i in fr[k]:
        start.append([i,1])

    for f in range(1,n+1):
        if f == k:
            continue

        visit = [0]*(n+1)
        visit[k] = 1

        q = deque(start)

        while True:
            spot, lev = q.popleft()

            if visit[spot]:
                continue

            visit[spot] = 1

            if spot == f:
                total += lev
                break

            for j in fr[spot]:
                q.append([j, lev+1])

    return total


n,m  = map(int,input().split(" "))
fr = [ [] for _ in range(n+1) ]
for i in range(m):
    a,b = map(int,input().split(" "))
    fr[a] = fr[a] + [b]
    fr[b] = fr[b] + [a]

bacon = [0]

for j in range(1,n+1):
    bacon.append(find_fr(j))

# print(bacon)
minnum = bacon[1]
index = 1

for a in range(2,n+1):
    if minnum > bacon[a]:
        minnum = bacon[a]
        index = a

print(index)

# print(fr)
# print('total :', bacon)