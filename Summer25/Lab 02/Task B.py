N, M, K = map(int,input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int,input().split()))

starting = 1
ending = M
best_starting = best_ending = 1
min_diff = float('inf')

while starting<=N and ending>=0:
    curr_sum = arr1[starting-1] + arr2[ending-1]
    curr_diff = abs(curr_sum - K)
    if curr_diff < min_diff:
        min_diff = curr_diff
        best_starting = starting
        best_ending = ending

    if curr_sum < K:
        starting += 1
    else:
        ending -= 1
print(best_starting, best_ending)
