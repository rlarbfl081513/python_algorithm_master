import sys
sys.setrecursionlimit(10**5)

def solution(k, num, links):
    root = [0] * len(num)
    for a, b in links:
        if a != -1:
            root[a] = 1
        if b != -1:
            root[b] = 1
    root_node = root.index(0)
    
    def dfs(node, limit):
        if node == -1:
            return 0, 0
            
        left_node = links[node][0]
        right_node = links[node][1]
        
        left_sum, left_cuts = dfs(left_node, limit)
        right_sum, right_cuts = dfs(right_node, limit)
        
        my_val = num[node]
        total_cuts = left_cuts + right_cuts 
        
        if my_val + left_sum + right_sum <= limit:
            return my_val + left_sum + right_sum, total_cuts
            
        elif my_val + min(left_sum, right_sum) <= limit:
            return my_val + min(left_sum, right_sum), total_cuts + 1
        
        else:
            return my_val, total_cuts + 2

    left = max(num)
    right = sum(num)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        
        _, cut_count = dfs(root_node, mid)
        
        if cut_count <= k - 1:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer