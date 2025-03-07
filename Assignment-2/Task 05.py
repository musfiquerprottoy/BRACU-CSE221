import sys
from bisect import bisect_left, bisect_right

def count_numbers_in_range(n, q, a, queries):
    a.sort()  # Ensure the list is sorted before using bisect
    results = []
    for x, y in queries:
        left_index = bisect_left(a, x)
        right_index = bisect_right(a, y)
        results.append(right_index - left_index)
    return results

# Read input
input = sys.stdin.read
data = input().splitlines()

n, q = map(int, data[0].split())
a = list(map(int, data[1].split()))
queries = [tuple(map(int, line.split())) for line in data[2:2 + q]]

# Get results
results = count_numbers_in_range(n, q, a, queries)

# Print results
print("\n".join(map(str, results)))
