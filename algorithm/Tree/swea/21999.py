

## 방법 1. 중위순회

# 왼쪽 자식이 있으면 왼쪽으로 가게하고 오른쪽 자식이 있으면 오른쪽으로 가게하기
# 더 이상 자식 노드가 없는 곳에 도착하면 그때부터 1씩 올라가도록

def tree(node):
    global n,li,val
    # 왼쪽 자식이 있으면
    if node*2 <= n:
        tree(node*2)

    val += 1
    li[node] = val

    # 오른쪽 자식이 있으면
    if node*2+1 <= n:
        return tree(node*2+1)

for tc in range(1,int(input())+1):
    n = int(input())
    li = [0]*(n+1)
    val = 0
    tree(1)
    # print(li)

    print(f'#{tc}',li[1],li[n//2])
    


## 방법 2. 중위순회

# 위 방식보다 코드는 짧지만 그냥 조건문을 없애서 짧아진거라 오히려 조건문을 거치지 않고 모든 값으로 재귀함수를 돌려버려서 시간이 더 든다. 

def tree(node):
    global n,num
 
    if node > n:
        return
 
    tree(node*2)
    value[node] = num
    num +=1
    tree(node * 2 + 1)
 
 
t = int(input())
for tc in range(1, 1+t):
    n = int(input())
    value = [0] * (n + 1)
    num = 1
    tree(1)
    print(f'#{tc} {value[1]} {value[n//2]}')