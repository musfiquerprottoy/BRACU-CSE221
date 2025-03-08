def longest_subarray(N, K, a):
    l = 0
    current_sum = 0
    max_len = 0

    for right in range(N):
        current_sum = current_sum + a[right]
        while current_sum > K: 
            current_sum =current_sum- a[l]
            l += 1
        
        max_len = max(max_len, right - l + 1)
    
    return max_len

N, K = map(int, input().split())
a = list(map(int, input().split()))

print(longest_subarray(N, K, a))
