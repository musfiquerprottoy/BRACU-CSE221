def longest_subarray_with_sum_at_most_k(n, k, arr):
    start = 0
    current_sum = 0
    max_length = 0

    for end in range(n):
        current_sum += arr[end]

        # Shrink the window from the left if the current sum exceeds K
        while current_sum > k:
            current_sum -= arr[start]
            start += 1

        # Update the maximum length of the valid subarray
        max_length = max(max_length, end - start + 1)

    return max_length

# Read input
n, k = map(int, input().split())
arr = list(map(int, input().split()))
# Get the result
result = longest_subarray_with_sum_at_most_k(n, k, arr)

# Print the result
print(result)