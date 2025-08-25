## 1. 회문 : 리스트를 뒤집어서 확인하기
# def word(ww):
#     if ww == ww[::-1]:
#         return 1
#     else:
#         return 0
#


## 2. 회문 :투포인터를 활용해서 풀기
def word(words):
    a,b = 0, len(words) - 1
    while a < b:
        if words[a] != words[b]:
            return 0
        a += 1
        b -= 1
    return 1


for tc in range(1,int(input())+1):
    w = list(input())
    print(f'#{tc}',word(w))
