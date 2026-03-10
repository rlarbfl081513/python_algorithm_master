import sys
input = sys.stdin.readline
from collections import deque

def con(k):
    global li,result

    result += 1
    li[k] = 1

    q = deque([k])

    while q:
        x = q.popleft()

        if dic.get(x):

            for i in dic[x]:
                if not li[i]:
                    q.append(i)
                    li[i] = 1

    if not li[k]:
        li[k] = 1


n,m = map(int, input().split(" "))
dic = {}
result = 0
li = [0]*(n+1)

for i in range(m):
    a,b = map(int,input().split(" "))
    dic[a] = dic.get(a,[]) + [b]
    dic[b] = dic.get(b, []) + [a]

for j in range(1,n+1):
    if not li[j]:
        con(j)

print(result)