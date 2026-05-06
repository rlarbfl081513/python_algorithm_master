def solution(X, Y):
    li = []
    dic ={}
    for i in range(10):
        dic[i] = [0,0]
    
    for x in X:
        dic[int(x)][0] += 1
        
    for y in Y:
        dic[int(y)][1] += 1
        
    for j in range(10):
        if dic[j][0] > 0 and dic[j][1] > 0:
            num = min(dic[j])
            li.extend([j for _ in range(num)])
    
    if len(li) == 0:
        return "-1"
    elif sum(li) == 0:
        return "0"
    else:
        li.sort()
        li.reverse()
        result = "".join(map(str,li))
        return result