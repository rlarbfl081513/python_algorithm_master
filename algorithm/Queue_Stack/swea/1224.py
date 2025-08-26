# 후위 계산기 만드는 계산기
def calculator(formula):
    stack = []  # 임시로 저장하는 것 부호
    result = []
    for i in formula:
        if i == '+':
            while stack and stack[-1] == '*':
                result.append(stack.pop())
            stack. append(i)
        elif i == '(':
            stack.append(i)
        elif i == '*':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            result.append(i)
 
    while stack:
        result.append(stack.pop())
    #print(result)
    return result
 
 
def cal(result):
    calculate = []
    for k in result:
        if k == '+' and calculate: # + 기호에 calculate 리스트가 안 비어 있으면 2개를 가져와서 계산함
            a = calculate.pop()
            b = calculate.pop()
            calculate.append(int(a) + int(b))
 
        elif k == '*' and calculate: # * 기호에 calculate 리스트가 안 비어 있으면 2개 가져와서 계산함
            a = calculate.pop()
            b = calculate.pop()
            calculate.append(int(a) * int(b))
 
        else:
            calculate.append(int(k))
 
    return calculate.pop()
 
for tc in range(1, 11):
    n = int(input())
    formula = list(input())
    # print(formula)
    ans = calculator(formula)
    print(f"#{tc}", cal(ans))