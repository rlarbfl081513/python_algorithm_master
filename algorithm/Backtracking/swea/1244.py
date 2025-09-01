import sys
sys.stdin = open("input.txt")

def suum(n):
    total = 0
    for i in range(len(n)):
        total += n[i]*(10**(len(n)-i-1))

    return total

def card(n,cnt):
    global m, maxnum,visit

    # set()에 넣기 위해 튜플형태로 변경
    key = tuple(n)
    # 이미 만들었던 조합이면 안할거임(백트래킹)
    if key in visit[cnt]:
        return
    # 새로운 조합이면 set에 추가
    visit[cnt].add(key)

    # 제한된 횟수만큼 했으면 맥스값 업데이트하기
    if cnt == m:
        maxnum = max(maxnum,suum(n))
        return

    # 한 번의 교환에서 i<j 두 자리만 골라 스왑하는 식을 위해 두개의 for문 사용
    for i in range(len(n)-1):
        for j in range(i+1, len(n)):
            n[i], n[j] = n[j], n[i]
            card(n,cnt+1)
            n[i], n[j] = n[j], n[i]


for tc in range(1,int(input())+1):
    n,m = map(int,input().split())
    n = [int(i) for i in str(n)]
    # print(n)
    visit = [set() for _ in range(m+1)]
    # print(visit)
    maxnum = 0
    card(n,0)
    print(f'#{tc}',maxnum)