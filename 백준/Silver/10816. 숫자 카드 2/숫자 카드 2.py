n = int(input())
n_arr = list(map(int, input().split(" ")))

m = int(input())
m_arr = list(map(int, input().split(" ")))

dic = {}

for i in n_arr:
    dic[i] = dic.get(i,0) + 1

for j in m_arr:
    print(dic.get(j,0), end=" ")
