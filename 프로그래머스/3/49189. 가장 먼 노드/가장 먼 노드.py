def solution(n, edge):
    # 가장 긴 간선이면서 같은 길이의 간선이 있으면 다 카운트
    # 각 노드끼리의 모든 길이를 구해서 마지막에 가장 긴 것 카운트
    
    dic = {}
    for i,j in edge:
        dic[i] = dic.get(i,[]) + [j]
        dic[j] = dic.get(j,[]) + [i]
        
    # print("전체 그림 :", dic)
    
    visit = [0]*(n+1)
    visit[1]=1
    
    distance = []
    for k in range(0,n+1):
        distance.append([0,k])
        
    start_list = [[1,0]]
    while len(start_list) > 0:
        # print("시작 리스트:",start_list)
        start,cnt = start_list.pop(0)
        # print("시작, 길이 : ",start,cnt)
        
        if visit[start]:
            distance[start][0] = cnt        
                    
        for i in dic.get(start,[]): 
            # print("연결노드 찾기 : ", i)
            if not visit[i]:
                start_list.append([i,cnt+1])
                visit[i] = 1
            
            
    # print(distance)
    # print("정답")
    distance.sort()
    max_num = distance[-1][0]
    total = 0
    for a,b in distance:
        if a == max_num:
            total += 1
    
    return total