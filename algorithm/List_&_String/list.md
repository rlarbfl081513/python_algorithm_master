# 알파벳
```python
    print(chr(97), chr(122))
    print(chr(65), chr(90))

    print()

    print(ord('a'), ord('z')) # 97 122
    print(ord('A'), ord('Z')) # 65 90
```

# DAT(Direct Address Table) 레퍼런스

## 개념

* **DAT = Direct Address Table**
  값 자체를 **인덱스**로 사용하는 배열.

  * 한마디로: *“값이 k인 요소를 `dat[k]`에 바로 표시/카운트”*
* 한국 알고리즘 학습에서 **카운팅 배열 / 체크 배열**이라고도 부름.

## 언제 쓰나

* 값의 **범위가 작고 정수**일 때 (예: 0\~100000)
* 빠른 **존재 여부 체크**, **빈도수 세기**, **최빈값/정렬 보조** 등에 최적
* 시간: O(1) 접근, 전체 초기화/순회 O(K) (K = 값의 범위 크기)

## 기본 형태

```python
# 존재 체크 (boolean)
MAX_V = 100000
dat = [0] * (MAX_V + 1)

# 값이 v를 봤다 표시
v = 345
dat[v] = 1

# v가 등장했는지?
exists = (dat[v] == 1)
```

```python
# 카운팅 (빈도)
MAX_V = 9
dat = [0] * (MAX_V + 1)

arr = [0,1,3,3,7,9,9,9]
for x in arr:
    dat[x] += 1

# 최빈값(동률이면 큰 값)
best_cnt = max(dat)             # 3
best_val = max(i for i,c in enumerate(dat) if c == best_cnt)  # 9
# best_cnt == 3, best_val == 9
```

## 대표 활용 패턴

### 1) 블랙리스트/존재 여부 체크

```python
# ID 범위: 0~100000
dat = [0] * 100001

# 블랙리스트 표기
blacklist = [13, 77, 50000]
for x in blacklist:
    dat[x] = 1

# 주민 ID가 블랙인지?
resident_id = 77
is_black = (dat[resident_id] == 1)  # True
```

### 2) 구간 개수/빈도 합 (프리픽스 응용)

```python
# 값 범위가 0~9인 배열에서 값이 [L..R]인 원소 개수 구하기
arr = [0,1,3,3,7,9,9,9]
dat = [0] * 10
for x in arr:
    dat[x] += 1                  # 각 값 빈도

# prefix[i] = (0..i) 값의 누적 빈도
prefix = [0]*10
run = 0
for i in range(10):
    run += dat[i]
    prefix[i] = run

L, R = 3, 9
count_LR = prefix[R] - (prefix[L-1] if L > 0 else 0)  # 6
# 값이 3~9 사이인 원소 개수
```

### 3) 문자열 문자 빈도

```python
s = "banana"
dat = [0] * 128  # ASCII 가정
for ch in s:
    dat[ord(ch)] += 1

# 'a' 빈도
dat[ord('a')]   # 3
```

### 4) 카운팅 정렬(Counting Sort) 보조

* dat에 각 값의 빈도를 누적해 두고 **안정 정렬** 수행 가능
* 값 범위가 작을수록 효과적

## 음수/큰 값 처리

### 1) 오프셋 사용 (음수 포함 시)

```python
# 값 범위: [-5000, 5000]
OFFSET = 5000
dat = [0] * (5000 + 5000 + 1)

def idx(v): return v + OFFSET

dat[idx(-3)] += 1
dat[idx(0)]  += 1
dat[idx(7)]  += 1
```

### 2) 좌표 압축 (스파스/범위가 매우 클 때)

```python
vals = [-1000, 1000000000, 42, 42]
uniq = sorted(set(vals))
to_idx = {v:i for i,v in enumerate(uniq)}  # 압축 매핑

dat = [0] * len(uniq)
for v in vals:
    dat[to_idx[v]] += 1
```

## 시간·공간 복잡도

* 조회/갱신: **O(1)**
* 초기화/전체 순회: **O(K)** (K=가능한 값의 가짓수)
* 공간: **O(K)**
  → 값 범위가 **너무 크면** 메모리 낭비 → **dict/set/압축** 고려

## 자주 하는 실수/팁

* **범위 확인 필수**: `dat = [0]*(max_value+1)` 에서 인덱스 초과 주의
* **2차원 DAT** 초기화 시 `[[0]*W]*H` 금지 (참조 공유)
  → `[[0]*W for _ in range(H)]` 사용
* **boolean vs int**: 존재만 필요하면 0/1로 충분 (메모리 절약)
* **sum 등 내장 불가 조건**에서도 유용 (직접 카운팅)
* \*\*입력 값이 드문드문(스파스)\*\*이면 dict가 더 효율적일 수 있음

## 짧은 예제 모음

```python
# 1) 존재 체크
MAX_V = 5
dat = [0]*(MAX_V+1)
for x in [1,4,4,2]:
    dat[x] = 1
print(dat)  # [0,1,1,0,1,0]

# 2) 빈도수
dat = [0]*(MAX_V+1)
for x in [1,4,4,2]:
    dat[x] += 1
print(dat)  # [0,1,1,0,2,0]

# 3) 최빈값(동률이면 큰 값 우선)
best_cnt = max(dat)                 # 2
best_val = max(i for i,c in enumerate(dat) if c == best_cnt)  # 4
print(best_cnt, best_val)  # 2 4
```

## 요약

* **DAT = 값→인덱스**로 바로 매핑하는 **체크/카운팅 배열**
* 값 범위가 **작고 정수**이면 최강: **존재 체크·카운트·구간집계·카운팅정렬**
* 범위 크거나 음수/희소일 때는 **오프셋·좌표 압축·dict/set** 고려

# strip
