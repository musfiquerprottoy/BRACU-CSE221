import sys
from collections import defaultdict, deque

sys.setrecursionlimit(200000 + 5)

def dfs_iterative(start):
    stack = [start]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            result.append(node)
            # Add neighbors in reverse order to maintain the correct order
            for neighbor in sorted(graph[node], reverse=True):
                if not visited[neighbor]:
                    stack.append(neighbor)

N, M = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))

graph = defaultdict(list)

for i in range(M):
    graph[u[i]].append(v[i])
    graph[v[i]].append(u[i])

visited = [False] * (N + 1)
result = []

dfs_iterative(1)

print(' '.join(map(str, result)))