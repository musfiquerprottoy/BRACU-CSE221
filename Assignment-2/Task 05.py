import bisect
import sys

# Read n and q
n, q = map(int, input().split())

# Read sorted array
arr = list(map(int, input().split()))

# Process each query
for _ in range(q):
    x, y = map(int, input().split())
    left = bisect.bisect_left(arr, x)
    right = bisect.bisect_right(arr, y)
    print(right - left)
