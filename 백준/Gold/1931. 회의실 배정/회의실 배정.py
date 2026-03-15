import sys

input = sys.stdin.readline

def meeting(ep,k,cnt):
    global result


    for j in range(k+1,n):
        if ep <= li[j][0]:
            cnt += 1
            ep = li[j][1]

    result = max(result,cnt)



n = int(input())
li = sorted([list(map(int,input().split(" "))) for _ in range(n)])
li.sort(key=lambda x: (x[1], x[0]))
result = 0

meeting(li[0][1],0,1)

print(result)