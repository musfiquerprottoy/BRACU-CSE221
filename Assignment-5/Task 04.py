from collections import deque, defaultdict


def bfs(graph, start, end):
    queue = deque([start])
    visited = {start: None}

    while queue:
        node = queue.popleft()

        if node == end:
            break

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited[neighbor] = node
                queue.append(neighbor)

    if end not in visited:
        return -1, []

    path = []
    while end is not None:
        path.append(end)
        end = visited[end]
    path.reverse()

    return len(path) - 1, path


def find_path(N, M, S, D, K, edges):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)

    length_S_to_K, path_S_to_K = bfs(graph, S, K)
    if length_S_to_K == -1:
        return -1

    length_K_to_D, path_K_to_D = bfs(graph, K, D)
    if length_K_to_D == -1:
        return -1

    total_length = length_S_to_K + length_K_to_D
    full_path = path_S_to_K[:-1] + path_K_to_D

    return total_length, full_path


N, M, S, D, K = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

result = find_path(N, M, S, D, K, edges)

if result == -1:
    print(-1)
else:
    length, path = result
    print(length)
    print(' '.join(map(str, path)))
