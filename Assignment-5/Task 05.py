def has_cycle(graph, N):
    state = [0] * (N + 1)

    for start in range(1, N + 1):
        if state[start] == 0:
            stack = [start]
            while stack:
                node = stack[-1]
                if state[node] == 0:
                    state[node] = 1
                    for neighbor in graph[node]:
                        if state[neighbor] == 0:
                            stack.append(neighbor)
                        elif state[neighbor] == 1:
                            return True
                else:
                    state[node] = 2
                    stack.pop()

    return False
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
if has_cycle(graph, N):
    print("YES")
else:
    print("NO")