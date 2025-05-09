import heapq

def minimize_danger(n, graph):
    danger = [float('inf')] * (n + 1)
    danger[1] = 0
    pq = [(0, 1)]

    while pq:
        curr_danger, u = heapq.heappop(pq)
        if curr_danger > danger[u]:
            continue
        for v, w in graph[u]:
            new_danger = max(curr_danger, w)
            if new_danger < danger[v]:
                danger[v] = new_danger
                heapq.heappush(pq, (new_danger, v))
    return danger

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w)) 

    danger = minimize_danger(n, graph)

    result = []
    for i in range(1, n + 1):
        if danger[i] == float('inf'):
            result.append(-1)
        else:
            result.append(danger[i])
    print(' '.join(map(str, result)))

solve()
