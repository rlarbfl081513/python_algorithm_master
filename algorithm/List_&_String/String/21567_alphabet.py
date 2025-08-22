
import sys
sys.stdin = open("input.txt")

## 1. 단어를 리스트로 보고 for문을 통해 알파벳 하나씩보면서 해당 알파벳 카운드 1씩 올리기

# print(chr(97), chr(122))
# print(chr(65), chr(90))

# print()

# print(ord('a'), ord('z')) # 97 122
# print(ord('A'), ord('Z')) # 65 90

def change_into_num(w):
    li = [0]*26

    for i in w:
        li[ord(i)-97] += 1

    return li

for tc in range(1,int(input())+1):
    word = input()
    new = change_into_num(word)
    print(f'#{tc}', " ".join(map(str,new)))


## 2. count를 활용
for tc in range(1,int(input())):
    w = input()
    print(f"#{tc}",end=" ")
    for i in range(26):
        print(w.count(chr(97+i)), end=" ")
    print()