def subtree(node):
    global count,visit,dic

    if node in dic:
        for j in dic[node]:
            if visit[j] == 0:
                visit[j] = 1
                count += 1
                subtree(j)


for tc in range(1,int(input())+1):
    e,n = map(int,input().split())
    arr = list(map(int,input().split()))
    count = 1
    visit = [0]*(e+2)
    dic = {}

    for i in range(0,e*2,2):
        a,b = arr[i], arr[i+1]
        dic[a] = dic.get(a,[]) + [b]
    # print(dic)

    visit[n] = 1
    subtree(n)
    print(f'#{tc}',count)