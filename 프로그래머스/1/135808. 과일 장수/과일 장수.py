def solution(k, m, score):
    score.sort()
    score.reverse()
    
    sum = 0
    
    box = len(score) // m
    start = m-1
    
    while box > 0:
        sum += score[start] * m
        start += m
        box -= 1

    return sum

        