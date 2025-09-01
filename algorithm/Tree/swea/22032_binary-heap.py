import sys
sys.stdin = open("input.txt")


# 1.번 방식
import heapq

def heap_def(node):
    global cnt

    if (node-1) // 2 >= 0:
        cnt += pq[(node-1) // 2]
    else:
        return

    heap_def((node-1) // 2)


t = int(input())
for tc in range(1,1+t):
    n = int(input())
    arr = list(map(int, input().split()))

    pq = []

    for e in arr:
        heapq.heappush(pq, e)

    cnt = 0

    heap_def(n-1)
    print(f'#{tc} {cnt}')
    # print(arr)


# 2.번 방식
import heapq

def node(num):
    global result, pq

    if num == 1:
        return result
    else:
        result += pq[num//2]
        return node(num//2)


t = int(input())
for tc in range(1,1+t):
    n = int(input())
    arr = list(map(int, input().split()))

    pq = []
    result = 0

    for e in arr:
        heapq.heappush(pq, e)

    pq = [0] + pq

    print(f'#{tc}',node(n))