# 구조 2
algorithm
 ┣ Graph
 ┃ ┣ 1_Basic_Navigation
 ┃ ┃ ┣ BFS_DFS.md
 ┃ ┃ ┗ Examples/
 ┃ ┣ 2_MST
 ┃ ┃ ┣ Kruskal.md
 ┃ ┃ ┗ Prim.md
 ┃ ┣ 3_Shortest_Path
 ┃ ┃ ┣ Dijkstra.md
 ┃ ┃ ┣ Bellman-Ford.md
 ┃ ┃ ┗ Floyd-Warshall.md
 ┃ ┣ 4_Network_Flow
 ┃ ┃ ┣ Ford-Fulkerson.md
 ┃ ┃ ┗ Edmonds-Karp.md
 ┃ ┗ 5_Tree_Graph
 ┃    ┣ Topological_Sort.md
 ┃    ┗ Union-Find.md

 ┣ DP_DynamicProgramming
 ┃ ┣ 1_Basic
 ┃ ┃ ┣ Fibonacci.md
 ┃ ┃ ┗ CoinChange.md
 ┃ ┣ 2_Classic
 ┃ ┃ ┣ LIS.md
 ┃ ┃ ┣ LCS.md
 ┃ ┃ ┣ Knapsack.md
 ┃ ┗ 3_Advanced
 ┃    ┣ Bitmask_DP.md
 ┃    ┗ Tree_DP.md

 ┣ Greedy
 ┃ ┣ ActivitySelection.md
 ┃ ┣ IntervalScheduling.md
 ┃ ┗ HuffmanCoding.md

 ┣ Sort
 ┃ ┣ Bubble.md
 ┃ ┣ Selection.md
 ┃ ┣ Insertion.md
 ┃ ┣ Merge.md
 ┃ ┣ Quick.md
 ┃ ┣ HeapSort.md
 ┃ ┗ Counting_Radix.md

 ┣ Search
 ┃ ┣ LinearSearch.md
 ┃ ┣ BinarySearch.md
 ┃ ┣ ParametricSearch.md
 ┃ ┗ TernarySearch.md

 ┣ Tree
 ┃ ┣ BinaryTree.md
 ┃ ┣ BST.md
 ┃ ┣ SegmentTree.md
 ┃ ┣ FenwickTree.md
 ┃ ┗ Trie.md

 ┣ Math
 ┃ ┣ Prime_Sieve.md
 ┃ ┣ GCD_LCM.md
 ┃ ┣ Modular_Arithmetic.md
 ┃ ┣ Combination_Permutation.md
 ┃ ┗ MatrixExponentiation.md

 ┣ Backtracking
 ┃ ┣ NQueen.md
 ┃ ┣ Sudoku.md
 ┃ ┗ Subset_Permutation.md

 ┣ DivideAndConquer
 ┃ ┣ MergeSort.md
 ┃ ┣ QuickSort.md
 ┃ ┗ MatrixChain.md

 ┣ List_&_String
 ┃ ┣ List
 ┃ ┃ ┣ SlidingWindow.md
 ┃ ┃ ┗ TwoPointers.md
 ┃ ┗ String
 ┃    ┣ KMP.md
 ┃    ┣ RabinKarp.md
 ┃    ┗ Manacher.md

 ┣ Queue_Stack
 ┃ ┣ Stack.md
 ┃ ┣ Queue.md
 ┃ ┣ Deque.md
 ┃ ┗ PriorityQueue.md

 ┣ Heap
 ┃ ┣ MinHeap.md
 ┃ ┣ MaxHeap.md
 ┃ ┗ Heapq_Usage.md

 ┣ BruteForce
 ┃ ┣ ExhaustiveSearch.md
 ┃ ┗ Bitmask.md

 ┗ Example_Problems
    ┣ BOJ/
    ┣ SWEA/
    ┗ Programmers/


# 구조 1
📌 1. 재귀 (Recursive)
- 기본 구조 및 개념
- 순열 / 조합 (next, backtracking으로 연결됨)
- DFS (재귀로 구현되는 경우 포함)
- DP (Top-down 방식)

📌 2. 탐색 알고리즘 (Search)
- 완전 탐색 (Brute Force)
- DFS (반복/재귀)
- BFS
- 백트래킹 (DFS + 가지치기 전략)
- 상태 공간 트리, 예제 패턴 정리

📌 3. 정렬 (Sort)
- 기본 정렬 (선택/삽입/버블)
- 고급 정렬 (퀵, 머지)
- Python 내장 정렬 & key 활용

📌 4. 자료구조
- 배열 / 리스트
- 스택 / 큐 / 덱
- 해시 / 딕셔너리 / 셋
- 우선순위 큐 / 힙
- 트리 / 그래프 표현 방법

📌 5. 그래프 알고리즘
1. 기본 탐색
   - DFS (재귀, 스택 구현)
   - BFS (큐 구현)

2. 연결 요소 판별
   - Union-Find (Disjoint Set)
   - 경로 압축, union by rank

3. 응용
   - 위상 정렬 (Topological Sort)
   - 최소 신장 트리 (Kruskal, Prim)
   - 최단 경로 (Dijkstra, Floyd, Bellman-Ford)
   - 그래프 + DP 조합 문제
     - 위상정렬 + DP
     - 트리 DP

📌 6. 동적 계획법 (DP)
- 개념 및 Bottom-up vs Top-down
- 기본 DP: 피보나치, 계단 오르기, 파스칼 삼각형
- 배낭 문제
- 문자열: LCS, LIS
- 그리디/탐색과 혼합되는 DP
- 그래프 위에서의 DP (그래프 파트와 연결)

📌 7. 수학 & 구현
- 최대공약수 / 최소공배수
- 에라토스테네스의 체
- 소수 판별
- 팩토리얼, 조합 공식
- 시뮬레이션 문제 구현

📌 8. 문자열 / 슬라이딩 윈도우
- 문자열 탐색, 정렬
- 투 포인터
- 슬라이딩 윈도우
- 아나그램, 회문, 문자열 DP

📌 9. 기타 알고리즘
- 비트마스킹
- 분할 정복
- 누적합 / 구간합
- 트라이 / 세그먼트 트리 등 (필요시)


