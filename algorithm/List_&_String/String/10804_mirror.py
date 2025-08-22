# 순서 바꾸는 함수
def change_num(li):
    new = []

    for i in range(len(li)-1,-1,-1):
        new.append(li[i])

    return mirror(new)

# 거울처럼 뒤집는 함수
def mirror(new):

    # 직접 뒤집는
    for j in range(len(new)):
        if new[j] == "b":
            new[j] = "d"
        elif new[j] == "d":
            new[j] = "b"
        elif new[j] == "p":
            new[j] = "q"
        elif new[j] == "q":
            new[j] = "p"

    return new


for tc in range(1, int(input())+1):
    w = input()
    result = change_num(w)
    print(f'#{tc}',"".join(map(str,result)))